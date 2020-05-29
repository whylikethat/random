text:
	python verses.py > verse.txt
	ls
	curl -X POST https://textbelt.com/text \
   --data-urlencode phone='4383454848' \
   --data-urlencode message="$(cat verse.txt)" \
   -d key=textbelt

clean:
	rm tempo.txt
	touch tempo.txt
	rm verse.txt
