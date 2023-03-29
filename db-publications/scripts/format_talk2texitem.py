import sys
import json
from operator import itemgetter
from datetime import datetime as dt

with open(sys.argv[1]) as f:
    db = json.load(f)

for e in sorted(db, key= lambda k: dt.strptime(k["TALK_DATE"], '%Y/%m/%d'), reverse=True):
    e["TALK_DATE_OBJ"] = dt.strptime(e["TALK_DATE"], '%Y/%m/%d')
    s = "\item "
    if e["PLACE"] == "online":
        s += "{TITLE}, {AUTHORS}, {CONF_NAME} ({CONF_DATE}), Online, {TALK_DATE}, {TALK_TYPE}.".format(**e)
    else:
        s += "{TITLE}, {AUTHORS}, {CONF_NAME} ({CONF_DATE}), {PLACE}, {COUNTRY}, {TALK_DATE}, {TALK_TYPE}.".format(**e)

    print(s)
    
