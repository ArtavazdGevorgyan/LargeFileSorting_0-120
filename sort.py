dct = dict()
for index in range(0, 121):
    dct[str(index)] = 0

with open("rawfile.txt") as file:
    line = file.readline().split(" ")[:-1]
    for i in line:
        dct[i]+=1
