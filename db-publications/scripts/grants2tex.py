import sys
import json

with open(sys.argv[1]) as f:
    db = json.load(f)


for e in sorted(db, key= lambda k: k["year"], reverse=True):
    s = "\item "
    s += "{year}年度  {研究種目} 「{研究課題名}」".format(**e)
    if "青木" in e["研究代表者"]:
        s += "・研究代表者"
    else:
        s += "・研究分担者"
    if "金額" in e:
        s += "・{金額}円".format(**e)
    print(s)
    
    

