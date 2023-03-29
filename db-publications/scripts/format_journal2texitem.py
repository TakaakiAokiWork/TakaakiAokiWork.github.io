import bibtexparser
import sys
import unicodedata
import datetime

with open(sys.argv[1]) as f:
    db = bibtexparser.load(f)
for e in db.entries:
    if "month" not in e:
        e["month"] = "jan"
    if e["month"].isnumeric():
        e["date"] = datetime.datetime.strptime("%s/%s/01" % (e["year"],e["month"]), "%Y/%m/%d").date()
    else:
        e["date"] = datetime.datetime.strptime("%s/%s/01" % (e["year"],e["month"]), "%Y/%b/%d").date()


def format_name_eng(splitted_name):
    list_namestr = []
    # detect me
    if (splitted_name['first'][0].lower() == 'takaaki' and splitted_name['last'][0].lower() == 'aoki'):
        return "\\underline{Takaaki Aoki}"

    list_namestr.extend(splitted_name['first'])
    if len(splitted_name["von"]) != 0:
        list_namestr.extend(splitted_name['von'])
    if len(splitted_name["jr"]) != 0:
        list_namestr.extend(splitted_name['jr'])
    list_namestr.extend(splitted_name['last'])
    return " ".join(list_namestr)
def format_name_jp(splitted_name):
    list_namestr = []
    # detect me
    if (splitted_name['first'][0].lower() == '高明' and splitted_name['last'][0].lower() == '青木'):
        return "\\underline{青木 高明}"
    list_namestr.extend(splitted_name['last'])
    list_namestr.extend(splitted_name['first'])
    return " ".join(list_namestr)

def format_name(splitted_name):
    if unicodedata.category(splitted_name['first'][0][0] ) == 'Lo':
        return format_name_jp(splitted_name)
    else:
        return format_name_eng(splitted_name)

def format_authors(authors):
    list_authors = []
    for person in e["author"]:
        person_parts = bibtexparser.customization.splitname(person)
        list_authors.append(format_name(person_parts))
    if len(list_authors) == 1:
        return list_authors[0] 
    if len(list_authors) == 2:
        return " \& ".join(list_authors)
    if len(list_authors) >= 3:
        return ", ".join(list_authors[0:-1]) + " \& " + list_authors[-1]



for e in sorted(db.entries, key= lambda k: k["date"], reverse=True):
    bibtexparser.customization.author(e)
    e["formatted_authors"] = format_authors(e["author"])
    #print(e)
    s = "\item "
    s += "{formatted_authors}, ``{title}'', ".format(**e)
    if "fulljournal" in e:
        s += "\\textbf{{{fulljournal}}}, ".format(**e)
    else:
        s += "\\textbf{{{journal}}}, ".format(**e)
    if "number" in e:
        s += "vol. {volume}({number}), {pages} ".format(**e)
    else:
        s += "vol. {volume}, {pages} ".format(**e)
    s += "({year}).".format(**e)
    print(s)
    
    

