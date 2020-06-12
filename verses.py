from random import randrange

f = open("bible.txt", "r")

# 61 books of the bible
books = ["Deuteronomy", "The Book of Joshua", "The Book of Judges", "The Book of Ruth", "The First Book of Samuel", "The Second Book of Samuel", "The Third Book of the Kings", "The Fourth Book of the Kings", "The First Book of the Chronicles", "The Second Book of the Chronicles", "Ezra", "The Book of Nehemiah", "The Book of Esther", "The Book of Job", "The Book of Psalms", "The Proverbs", "Ecclesiastes", "The Song of Solomon", "The Book of the Prophet Isaiah", "The Book of the Prophet Jeremiah", "The Lamentations of Jeremiah", "The Book of the Prophet Ezekiel", "The Book of Daniel", "Hosea", "Joel", "Amos", "Obadiah", "Jonah", "Micah", "Nahum", "Habakkuk", "Zephaniah", "Haggai", "Zechariah", "Malachi", "The Gospel According to Saint Matthew", "The Gospel According to Saint Mark", "The Gospel According to Saint Luke", "The Gospel According to Saint John", "The Acts of the Apostles", "The Epistle of Paul the Apostle to the Romans", "The First Epistle of Paul the Apostle to the Corinthians", "The Second Epistle of Paul the Apostle to the Corinthians", "The Epistle of Paul the Apostle to the Galatians", "The Epistle of Paul the Apostle to the Ephesians", "The Epistle of Paul the Apostle to the Colossians", "The First Epistle of Paul the Apostle to the Thessalonians", "The Second Epistle of Paul the Apostle to the Thessalonians", "The First Epistle of Paul the Apostle to Timothy", "The Second Epistle of Paul the Apostle to Timothy", "The Epistle of Paul the Apostle to Titus", "The Epistle of Paul the Apostle to Philemon", "The Epistle of Paul the Apostle to the Hebrews", "The General Epistle of James", "The First Epistle General of Peter", "The Second General Epistle of Peter", "The First Epistle General of John", "The Second Epistle General of John" , "The Third Epistle General of John", "The General Epistle of Jude", "The Revelation of Saint John the Devine"]

book = randrange(61)
randombook = books[book]
currentbook = open("tempo.txt", "a")

for line in f:
    if randombook in line:
        print("From " + randombook + ": " + '\n')
        while books[book+1] not in line:
            currentbook.write(line)
            line = next(f)

        currentbook.close()

count = len(open("tempo.txt").readlines(  ))
randomline = randrange(count)
verse = open("tempo.txt", "r")
for i, line in enumerate(verse):
    if i == randomline:
        while line[0].isdigit() == False:
            line = next(verse)

        print(line)
        while "." not in line:
            line = next(verse)
            print(line)



verse.close()
f.close()
