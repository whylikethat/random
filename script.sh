python verses.py > verse.txt
sed '/^[[:space:]]*$/d' verse.txt > new.txt
curl -X POST https://textbelt.com/text \
   --data-urlencode phone='4383454848' \
   --data-urlencode message="$(cat new.txt)" \
   -d key=textbelt

python notification.py
# Replace the phone number with the recepient phone number
