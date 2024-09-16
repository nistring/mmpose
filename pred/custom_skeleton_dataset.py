import numpy as np
import json
import cv2
import os
import pandas as pd
from sklearn.model_selection import train_test_split
import pickle
from tqdm import tqdm
import math

# Parameters
test_size = 0.33
random_state = 0

df = pd.read_excel("../data/GM_data_index_final.xlsx", usecols="C,J,X,Z")
df.dropna(subset=["video name", 'Assess'], inplace=True)
df = df[df.quality == 1]

fidgety_train, fidgety_test, writhing_train, writhing_test = [], [], [], []
df.set_index("video name", inplace=True)
df_train = df[df.start.isnull()]
df_test = df.dropna(subset="start")
for index, row in df_train.iterrows():
    if row["Assess"] in ["NL", "PR", "CS"]:
        writhing_train.append(index)
    else:
        fidgety_train.append(index)
for index, row in df_test.iterrows():
    if row["Assess"] in ["NL", "PR", "CS"]:
        writhing_test.append(index)
    else:
        fidgety_test.append(index)

# Normal 0, abnormal 1
assess2label = {"(-)": 1, "(+/-)":1, "(+)": 0, "(++)":0, "NL":0, "PR":1, "CS":1}
FPS = 30
clip_len = FPS * 30 # at least 30 seconds

for keypoints in ["17", "29"]:

    dataset = {
        "split": {
            "fidgety_train": fidgety_train,
            "fidgety_test": fidgety_test,
            "writhing_train": writhing_train,
            "writhing_test": writhing_test,
        },
        "annotations":[]
    }

    for file in df.index:
        with open(f"{keypoints}/results_{file}.json", "r") as f:
            anno = json.load(f)["instance_info"]

        cur_start, max_start, cur_len, max_len = 0, 0, 0, 0
        for i, x in enumerate(anno):
            if len(x["instances"]) == 1:
                if cur_len == 0:
                    cur_start = i
                cur_len += 1
            else:
                if cur_len > max_len:
                    max_len = cur_len
                    max_start = cur_start
                cur_len = 0

        if max_len >= clip_len:
            # Get video dimension
            cap = cv2.VideoCapture(f"../data/videos/{file}.mp4")
            print(f"../data/videos/{file}.mp4 processing ...")
            if cap.isOpened():
                shape  = (int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)), int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)))
                fps = cap.get(cv2.CAP_PROP_FPS)
                if fps < 29 or fps > 31:
                    continue
            del cap

            keypoint, keypoint_score = [], []
            for i in range(max_start, max_start + max_len + 1):
                instance = anno[i]["instances"]
                keypoint.append(instance[0]["keypoints"])
                keypoint_score.append(instance[0]["keypoint_scores"])

            dataset["annotations"].append(
                {
                    'frame_dir': file,
                    'label': assess2label[df.loc[file, "Assess"]],
                    'img_shape': shape,
                    'original_shape': shape,
                    'total_frames': len(keypoint),
                    'keypoint': np.array([keypoint]),
                    "keypoint_score": np.array([keypoint_score])
                }
            )

    with open(f"GMA{keypoints}.pkl", 'wb') as file:
        pickle.dump(dataset, file)