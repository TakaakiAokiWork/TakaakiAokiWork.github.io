# coding: utf-8
from __future__ import unicode_literals
import sys
import json
import pandas as pd
from operator import itemgetter
from datetime import datetime as dt

df = pd.read_json(sys.argv[1], convert_dates=["TALK_DATE"])

print('## Talks')

# year(年度)カラムを追加
df['Year'] = df['TALK_DATE'].dt.year
df.loc[df['TALK_DATE'].dt.month < 4, 'Year'] = df['TALK_DATE'].dt.year - 1
df['TALK_DATE'] = df['TALK_DATE'].dt.strftime("%Y/%m/%d")

grp = df.groupby("Year")
for year in sorted(grp.groups, reverse=True):
    print("#### %d年度" % year)
    print("<ol>")
    for i,d in grp.get_group(year).sort_values("TALK_DATE", ascending=False).iterrows():
        if len(d["ADDRESS"]) > 0:
            print("<li>{TITLE}, {AUTHORS}, {CONF_NAME}({CONF_DATE}), {TALK_DATE}, {PLACE}, {ADDRESS}, {COUNTRY}, {TALK_TYPE}. </li>".format(**d))
        else:
            print("<li>{TITLE}, {AUTHORS}, {CONF_NAME}({CONF_DATE}), {TALK_DATE}, {PLACE}, {TALK_TYPE}. </li>".format(**d))
    print("</ol>")

