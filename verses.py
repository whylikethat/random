from random import randrange

f = open("bible.txt", "r")

# 26 books of the bible
books = ["The Gospel According to Saint Matthew","The Gospel According to Saint Mark","The Gospel According to Saint Luke","The Gospel According to Saint John","The Acts of the Apostles","The Epistle of Paul the Apostle to the Romans","The First Epistle of Paul the Apostle to the Corinthians","The Second Epistle of Paul the Apostle to the Corinthians","The Epistle of Paul the Apostle to the Galatians","The Epistle of Paul the Apostle to the Ephesians","The Epistle of Paul the Apostle to the Colossians","The First Epistle of Paul the Apostle to the Thessalonians","The Second Epistle of Paul the Apostle to the Thessalonians","The First Epistle of Paul the Apostle to Timothy","The Second Epistle of Paul the Apostle to Timothy", "The Epistle of Paul the Apostle to Titus","The Epistle of Paul the Apostle to Philemon","The Epistle of Paul the Apostle to the Hebrews","The General Epistle of James","The First Epistle General of Peter","The Second General Epistle of Peter","The First Epistle General of John","The Second Epistle General of John" ,"The Third Epistle General of John","The General Epistle of Jude","The Revelation of Saint John the Devine"," "]

book = randrange(25)
randombook = books[book]
currentbook = open("tempo.txt", "w")

for line in f:
    if randombook in line:
        print("From " + randombook + ": " + '\n')
        while books[book+1] not in line:
            currentbook.write(line)
            line = next(f)

        currentbook.close()


count = len(open("tempo.txt").readlines(  )) - 1
randomline = randrange(count)
verse = open("tempo.txt", "r")
endresult = ""
for i, line in enumerate(verse):
    if i == randomline:
        while line[0].isdigit() == False:
            line = next(verse)

        endresult += line
        line = next(verse)
        while line[0].isdigit() == False:
            endresult += line
            print(i)
            if i != count: # modify this part because it keeps getting more lines than the chapter
                line = next(verse)
            else:
                break



print(endresult)
verse.close()
f.close()
