import numpy as np
import json
import cv2
import pandas as pd
import pickle

# Load the dataset from an Excel file
df = pd.read_excel("../data/GM_data_index_final.xlsx", usecols="C,J,X,Z")
df.dropna(subset=["video name", 'Assess'], inplace=True)
df = df[df.quality == 1]

# Initialize lists to hold training and testing data
fidgety_train, fidgety_test, writhing_train, writhing_test = [], [], [], []
df.set_index("video name", inplace=True)
df_train = df[df.start.isnull()]
df_test = df.dropna(subset="start")

# Split the data into training and testing sets based on the 'Assess' column
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

FPS = 30
clip_len = FPS * 60 # at least 60 seconds

# Process keypoints for different configurations
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

    # Iterate over each video file in the dataset
    for file in df.index:
        with open(f"{keypoints}/results_{file}.json", "r") as f:
            anno = json.load(f)["instance_info"]

        # Get video dimension
        cap = cv2.VideoCapture(f"../data/videos/{file}.mp4")
        print(f"../data/videos/{file}.mp4 processing ...")
        if cap.isOpened():
            shape  = (int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)), int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)))
            fps = cap.get(cv2.CAP_PROP_FPS)
            if fps < 29 or fps > 31:
                continue
        del cap

        keypoint, keypoint_score, indices = [], [], []
        for i, x in enumerate(anno):
            instance = x["instances"]
            if len(instance) == 1:
                keypoint.append(instance[0]["keypoints"])
                keypoint_score.append(instance[0]["keypoint_scores"])
                indices.append(i)

        # Only include videos with enough keypoints
        if len(keypoint) >= clip_len:
            dataset["annotations"].append(
                {
                    'frame_dir': file,
                    'label': df.loc[file, "Assess"],
                    'img_shape': shape,
                    'original_shape': shape,
                    'total_frames': len(keypoint),
                    'keypoint': np.array([keypoint]),
                    "keypoint_score": np.array([keypoint_score]),
                    "indices": np.array(indices)
                }
            )

    # Save the dataset to a pickle file
    with open(f"GMA{keypoints}.pkl", 'wb') as file:
        pickle.dump(dataset, file)