import sys
import datetime
import json
import pandas as pd 
import csv

with open(sys.argv[1]) as f:
    db = json.load(f)

for entry in db:
    entry["アクション名"] = "insert"
    entry["アクションタイプ"] = "similar_merge"
    entry["類似業績マージ優先度"] = "input_data"
    entry["ID"] = ""

df = pd.DataFrame(db)
df = df.drop("MENDAN_AFF",axis=1)
df = df.drop("MENDAN_NAME",axis=1)
df = df.drop("WEB",axis=1)
df = df.drop("url",axis=1)

with open(sys.argv[2], "w") as f:
    print("presentations", file=f)
    df.to_csv(f, index=None, quoting=csv.QUOTE_NONNUMERIC)

