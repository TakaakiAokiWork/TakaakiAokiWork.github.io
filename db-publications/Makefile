
publications:
	echo "# Preprint" > tmp/Publications.preprint
	python scripts/journal2html.py preprint.bib >> tmp/Publications.preprint
	echo "# Articles" > tmp/Publications.articles
	python scripts/journal2html.py Articles.bib >> tmp/Publications.articles
	echo "# Articles in Japanese" > tmp/Publications.jparticles
	python scripts/journal2html.py ArticlesWithoutReview.bib >> tmp/Publications.jparticles
	echo "# Reviews" > tmp/Publications.review
	python scripts/journal2html.py Review.bib >> tmp/Publications.review
	echo "# Proceedings" > tmp/Publications.proc
	python scripts/journal2html.py Proceedings.bib >> tmp/Publications.proc
	echo "# Research grants" > tmp/Publications.grant
	echo "## Grants-in-Aid for Scientific Research from JSPS: 科研費他" >> tmp/Publications.grant
	python scripts/grants2html.py Grant.json >> tmp/Publications.grant
	echo "## Other funds" >> tmp/Publications.grant
	python scripts/grants2html.py GrantOthers.json >> tmp/Publications.grant
	python scripts/parse_talk.py Talk.json  > tmp/Publications.talk
	cat ../docs/Publications.head tmp/Publications.preprint tmp/Publications.articles tmp/Publications.jparticles Publications.book tmp/Publications.review tmp/Publications.proc tmp/Publications.grant tmp/Publications.talk Publications_talk_before_2015.htm > ../docs/Publications.md

