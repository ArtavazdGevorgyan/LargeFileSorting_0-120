import random
#import os

with open("rawfile.txt", "w") as file:
    for line in range(0, 40000000):
        for i in range(0, 32):
            file.write(str(random.randint(0, 120)) + " ")
        file.write("\n")

#print(os.path.getsize("rawfile.txt"))

