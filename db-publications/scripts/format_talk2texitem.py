# coding: utf-8
from __future__ import unicode_literals
import sys
import json
import pandas as pd
from operator import itemgetter
from datetime import datetime as dt
import pycountry

df = pd.read_json(sys.argv[1], convert_dates=["発表年月日"])

# year(年度)カラムを追加
df['Year'] = df['発表年月日'].dt.year
df.loc[df['発表年月日'].dt.month < 4, 'Year'] = df['発表年月日'].dt.year - 1
df['発表年月日'] = df['発表年月日'].dt.strftime("%Y/%m/%d")


def is_exists_key(key, entry):
    value = entry.get(key, "")
    if pd.isna(value):
        return False
    if len(value) == 0:
        return False
    else:
        return True


def parse(entry):
    d = dict()
    print(entry, file=sys.stderr)

    if is_exists_key("タイトル(日本語)",entry):
        d["title"]  = entry["タイトル(日本語)"]
    else:
        d["title"]  = entry["タイトル(英語)"]

    if is_exists_key("講演者(日本語)", entry):
        d["author"]  = entry["講演者(日本語)"]
    else:
        d["author"]  = entry["講演者(英語)"]

    if is_exists_key("講演者(日本語)", entry):
        d["author"]  = entry["講演者(日本語)"]
    else:
        d["author"]  = entry["講演者(英語)"]

    if is_exists_key("会議名(日本語)" , entry):
        d["conference"]  = entry["会議名(日本語)"]
    else:
        d["conference"]  = entry["会議名(英語)"]

    if is_exists_key("開催地(日本語)" , entry):
        d["place"]  = entry["開催地(日本語)"]
    else:
        d["place"]  = entry["開催地(英語)"]

    d["date_from"] = dt.strptime(entry['開催年月日(From)'], '%Y-%m-%d')
    d["date_talk"] = entry['発表年月日']
    if entry["開催年月日(To)"] != "":
        d["date_to"] = dt.strptime(entry['開催年月日(To)'], '%Y-%m-%d')
    else:
        d["date_to"] = d["date_from"]

    d["talk_type"] = entry["発表種別"].replace("_presentation","")
    d["country"] = pycountry.countries.get(alpha_3=entry['国・地域']).name
    return(d)



def escape_tex(text):
    """
    Escapes special TeX characters in a Python string.
    
    :param text: The input string.
    :return: A string with TeX special characters escaped.
    """
    if text is None:
        return ""
        
    # The order matters! Backslash must be first.
    replacements = [
        (r"\\", r"\textbackslash{}"),  # Must be first
        ("&", r"\&"),
        ("%", r"\%"),
        ("$", r"\$"),
        ("#", r"\#"),
        ("_", r"\_"),
        ("{", r"\{"),
        ("}", r"\}"),
        ("~", r"\textasciitilde{}"),
        ("^", r"\textasciicircum{}"),
    ]
    
    for old, new in replacements:
        text = text.replace(old, new)
        
    return text

for i,entry in df.sort_values("発表年月日", ascending=False).iterrows():
    d = parse(entry)
    d["date_from"] = d["date_from"].strftime("%Y/%m/%d")
    d["date_to"] = d["date_to"].strftime("%Y/%m/%d")
    s = "\item {title}, {author}, {conference}({date_from}-{date_to}), {date_talk}, {place}, {country}, {talk_type}".format(**d)
    # Replace "_" with r"\_"
    tex_safe_string = escape_tex(s)
    print(tex_safe_string)
