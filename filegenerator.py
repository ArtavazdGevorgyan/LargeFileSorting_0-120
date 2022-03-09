import random
import os
# 1 bar@ zbaxacnuma mijinum 3.17  byte taracq
file = open("rawfile.txt", "w")

for line in range(0, 4000):  # 40000000
    for i in range(0, 25):
        file.write(str(random.randint(0, 120)) + " ")
    file.write("\n")
file.close()

print(os.path.getsize("rawfile.txt"))

"""with open( "rawfile.txt" )as file:
    
    for i in 200:
        file.write()
"""
