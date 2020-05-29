python verses.py > verse.txt
curl -X POST https://textbelt.com/text \
   --data-urlencode phone='4383454848' \
   --data-urlencode message="$(cat verse.txt)" \
   -d key=textbelt
