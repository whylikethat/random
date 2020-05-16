from random import randrange

f = open("bible.txt", "r")

randomline = randrange(99817)
for i, line in enumerate(f):
    if i == randomline:
        while line[0].isdigit() == False:
            line = next(f)

        print(line)
        while "." not in line:
            line = next(f)
            print(line)

f.close()
