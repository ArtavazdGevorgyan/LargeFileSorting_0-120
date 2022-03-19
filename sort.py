#import os
dct = dict()
for index in range(0, 121):
    dct[index] = 0

with open("rawfile.txt", "r") as file:
    for line in file:
        line = line.strip(' \n')
        lst = list(line.split(" "))
        for i in lst:
            dct[int(i)] += 1
nl=0
with open('sortedfile.txt', 'w') as file:
    for i in dct.keys():
        for j in range(0, dct[i]):
            file.write(str(i) + " ")
            nl+=1
            if nl%32==0:
                file.write("\n")

#print(os.path.getsize("sortedfile.txt"))
