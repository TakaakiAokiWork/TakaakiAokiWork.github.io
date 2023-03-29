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
        return "<span id='me'>Takaaki Aoki</span>"

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
        return "<span id='me'>青木 高明</span>"
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
        return " &amp; ".join(list_authors)
    if len(list_authors) >= 3:
        return ", ".join(list_authors[0:-1]) + " \& " + list_authors[-1]



print("{::nomarkdown}")
print("<div id='publication'>" )
print("<ol>")
for e in sorted(db.entries, key= lambda k: k["date"], reverse=True):
    bibtexparser.customization.author(e)
    e["formatted_authors"] = format_authors(e["author"])
    s = "<li>"
    s += "<span id='title'>{title}</span>, ".format(**e)
    s += "{formatted_authors}, ".format(**e)
    if "fulljournal" in e:
        s += "<em>{fulljournal}</em>, ".format(**e)
    else:
        s += "<em>{journal}</em>, ".format(**e)
    if "number" in e:
        s += "vol. {volume}({number}), {pages} ".format(**e)
    else:
        s += "vol. {volume}, {pages} ".format(**e)
    s += "({year}).".format(**e)
    if "pdf" in e:
        s += "<br><a href=pdfs/{pdf}> <button type='button' class='btn btn-primary'>Fulltext (free)</button></a>".format(**e)
    if "doi" in e:
        s += "<br>DOI: <a href=https://doi.org/{doi}>{doi}</a>".format(**e)
    if "url" in e:
        if "crid" in e["url"]:
            s += "<br>Link to <a href={url}> CiNii database</a>".format(**e)

    print(s)
    
print("</ol>")
print("</div>")
print("{:/nomarkdown}\n\n")
    

