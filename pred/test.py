import pickle
from collections import Counter
from sklearn.model_selection import train_test_split

# with open("GMA17.pkl", "rb") as f:
#     GMA17 = pickle.load(f)
# with open("GMA29.pkl", "rb") as f:
#     GMA29 = pickle.load(f)

# assert GMA17["split"]["writhing_train"] == GMA29["split"]["writhing_train"]
# assert GMA17["split"]["writhing_test"] == GMA29["split"]["writhing_test"]
# assert GMA17["split"]["fidgety_train"] == GMA29["split"]["fidgety_train"]
# assert GMA17["split"]["fidgety_test"] == GMA29["split"]["fidgety_test"]

# del GMA17, GMA29

for path in ["GMA17.pkl", "GMA29.pkl"]:
    with open(path, "rb") as f:
        data = pickle.load(f)

    # for mov in ["writhing", "fidgety"]:
    #     data_list = data["split"][f"{mov}_train"] + data["split"][f"{mov}_test"]
    #     neg_list, pos_list = [], []
    #     for x in data["annotations"]:
    #         if x["frame_dir"] in data_list:
    #             if x["label"] == 0:
    #                 neg_list.append(x["frame_dir"])
    #             else:
    #                 pos_list.append(x["frame_dir"])

    #     neg_train, neg_test = train_test_split(
    #         neg_list, test_size=0.25, random_state=0)
    #     pos_train, pos_test = train_test_split(
    #         pos_list, test_size=0.25, random_state=0)
    #     data["split"][f"{mov}_train"] = neg_train + pos_train
    #     data["split"][f"{mov}_test"] = neg_test + pos_test

    data_list = data["split"]["writhing_train"]
    label_list = []
    for x in data["annotations"]:
        if x["frame_dir"] in data_list:
            label_list.append(x["label"])
    print(Counter(label_list))

    data_list = data["split"]["writhing_test"]
    label_list = []
    for x in data["annotations"]:
        if x["frame_dir"] in data_list:
            label_list.append(x["label"])
    print(Counter(label_list))

    data_list = data["split"]["fidgety_train"]
    label_list = []
    for x in data["annotations"]:
        if x["frame_dir"] in data_list:
            label_list.append(x["label"])
    print(Counter(label_list))

    data_list = data["split"]["fidgety_test"]
    label_list = []
    for x in data["annotations"]:
        if x["frame_dir"] in data_list:
            label_list.append(x["label"])
    print(Counter(label_list))

    # with open(f"sorted_{path}", "wb") as f:
    #     pickle.dump(data, f)