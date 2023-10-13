import os
import json
import pandas as pd

df = {}
work_dir = 'work_dirs'
for config in os.listdir(work_dir):
    config_dir = os.path.join(work_dir, config)
    for exp in os.listdir(config_dir):
        exp_dir = os.path.join(config_dir, exp)
        if os.path.isdir(exp_dir):
            for file in os.listdir(exp_dir):
                if '.json' in file:
                    with open(os.path.join(exp_dir, file), 'r') as f:
                        try:
                            df[config] = json.load(f)
                        except:
                            print(config_dir, file, "can't be open.")

summary = pd.DataFrame(df)
summary.to_csv('results.csv')