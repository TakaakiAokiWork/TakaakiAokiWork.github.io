# coding: utf-8
from __future__ import unicode_literals
import sys
import json
import pandas as pd
from operator import itemgetter
from datetime import datetime as dt
import pycountry

df = pd.read_json(sys.argv[1], convert_dates=["発表年月日"])

print('## Talks')

# year(年度)カラムを追加
df['Year'] = df['発表年月日'].dt.year
df.loc[df['発表年月日'].dt.month < 4, 'Year'] = df['発表年月日'].dt.year - 1
df['発表年月日'] = df['発表年月日'].dt.strftime("%Y-%m-%d")

grp = df.groupby("Year")
for year in sorted(grp.groups, reverse=True):
    print("#### %d年度" % year)
    print("<ol>")
    for i,d in grp.get_group(year).sort_values("発表年月日", ascending=False).iterrows():
        s = "<li>{タイトル(日本語)}, {講演者(日本語)}".format(**d)
        if d["開催年月日(To)"] != "":
            s += "{会議名(日本語)}({開催年月日(From)}-{開催年月日(To)}), {発表年月日}".format(**d)
        else:
            s += "{会議名(日本語)}({開催年月日(From)}), {発表年月日}".format(**d)
        if len(d["開催地(日本語)"]) > 0:
            d["country"] = pycountry.countries.get(alpha_3=d['国・地域']).name
            s += ",{開催地(日本語)}, {country}".format(**d)
        talk_type = d["会議種別"].replace("_presentation","")
        s += "," +  talk_type + "</li>"
        print(s)
    print("</ol>\n\n")

