import random
import os

# Tiv@ zbaxacnuma mijinum 3.17  byte taracq

file = open("rawfile.txt", "w")
for line in range(0, 40000000):
    for i in range(0, 32):
        file.write(str(random.randint(0, 120)) + " ")
    file.write("\n")

file.close()

print(os.path.getsize("rawfile.txt"))

