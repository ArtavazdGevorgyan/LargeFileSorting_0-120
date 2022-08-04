#import os

dct = {i : 0 for i in range(121)}

with open("rawfile.txt", "r") as file:
    for line in file:
        line = line.strip(' \n')
        lst = list(line.split(" "))
        for i in lst:
            dct[int(i)] += 1
newline = 0
with open('sortedfile.txt', 'w') as file:
    for i in dct.keys():
        for j in range(0, dct[i]):
            file.write(str(i) + " ")
            newline += 1
            if newline == 32:
                newline = 0
                file.write("\n")

#print(os.path.getsize("sortedfile.txt"))
