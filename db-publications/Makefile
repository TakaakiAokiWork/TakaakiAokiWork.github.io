
publications:
	python scripts/parse_talk.py Talk.json  > tmp/Publications.talk
	echo "# Research grants" > tmp/Publications.grant
	echo "## Grants-in-Aid for Scientific Research from JSPS: 科研費他" >> tmp/Publications.grant
	python scripts/grants2html.py Grant.json >> tmp/Publications.grant
	cat ../docs/Publications.head tmp/Publications.grant tmp/Publications.talk Publications_talk_before_2015.htm > ../docs/Publications.md

