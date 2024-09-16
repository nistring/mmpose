import pickle

with open("GMA17.pkl", "rb") as f:
    data = pickle.load(f)

print(data["split"]["writhing_train"])
