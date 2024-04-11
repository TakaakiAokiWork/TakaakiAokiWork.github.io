import sys
import datetime
import json

with open(sys.argv[1]) as f:
    db = json.load(f)


def format_talk_type(txt):
    lower_txt = txt.lower()
    if lower_txt == "oral":
        return "oral_presentation"
    elif lower_txt == "poster":
        return "poster_presentation"
    elif lower_txt == "invited":
        return "invited_oral_presentation"
    else:
        print(txt, file = sys.stderr)
        return "others"

def format_conf_date(txt):
    if "-" in txt:
        start,end = txt.split("-")
        start_date = datetime.datetime.strptime(start.strip(), '%Y/%m/%d')
        if "/" in end:
            end_date = datetime.datetime.strptime( str(start_date.year) + "/" +  end.strip(), '%Y/%m/%d')
        else:
            end_date = datetime.date(start_date.year, start_date.month, int(end) )
        return [start_date.strftime("%Y-%m-%d"), end_date.strftime("%Y-%m-%d")]
    else:
        date = datetime.datetime.strptime(txt, "%Y/%m/%d")
        return [date.strftime("%Y-%m-%d"), ""]

def copy_if_ascii(txt):
    if txt.isascii():
        return(txt)
    else:
        return("")
def format_country(txt):
    if txt == "":
        return "JPN"
    if txt.lower() == "japan":
        return "JPN"
    if txt.lower() == "usa":
        return "USA"
    if txt.lower() == "belgium":
        return "BEL"
    if txt.lower() == "beligium":
        return "BEL"
    if txt.lower() == "united kingdom":
        return "GBR"
    if txt.lower() == "korea":
        return "PRK"
    if txt.lower() == "austria":
        return "AUT"
    if "Netherlands" in txt:
        return "NLD"
    print("unknown country code", txt)
    exit(1)
    return("")

for entry in db:
    entry["タイトル(日本語)"] = entry.pop("TITLE")
    entry["タイトル(英語)"] = entry["タイトル(日本語)"]
    entry["講演者(日本語)"] = entry.pop("AUTHORS")
    entry["講演者(英語)"] = copy_if_ascii( entry["講演者(日本語)"])
    entry["会議名(日本語)"] = entry.pop("CONF_NAME")
    entry["会議名(英語)"] = copy_if_ascii( entry["会議名(日本語)"])
    entry["開催地(日本語)"] = (entry.pop("ADDRESS") + " " + entry.pop("PLACE")).strip()
    entry["開催地(英語)"] = copy_if_ascii( entry["開催地(日本語)"])
    entry["発表年月日"] = datetime.datetime.strptime(entry.pop("TALK_DATE"), "%Y/%m/%d").strftime("%Y-%m-%d")
    entry["開催年月日(From)"], entry["開催年月日(To)"] = format_conf_date(entry.pop("CONF_DATE"))
    entry["国・地域"] = format_country(entry.pop("COUNTRY"))
    entry["会議種別"] = format_talk_type(entry.pop("TALK_TYPE"))

json.dump(db, sys.stdout, indent=2, ensure_ascii=False)
#print(db)

