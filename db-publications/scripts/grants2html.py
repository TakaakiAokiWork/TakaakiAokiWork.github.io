import sys
import json

with open(sys.argv[1]) as f:
    db = json.load(f)


print("{::nomarkdown}\n<ol>")
for e in sorted(db, key= lambda k: k["year"], reverse=True):
    s = "<li> "
    s += "{year}年度 「{研究課題名}」<br> {研究種目}".format(**e)
    if "青木" in e["研究代表者"]:
        s += "・研究代表者"
    else:
        s += "・研究分担者"
    if "url" in e:
        s += "<br> <a href={url}>課題番号 {ID}</a>".format(**e)
    print(s)
print("</ol>\n{:/nomarkdown}\n\n")
    
    

