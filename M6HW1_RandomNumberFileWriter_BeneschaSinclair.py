#M6HW1 - Random Number File Writer
#July 14, 2017
#CTI110 M6HW1 - Random Number File Writer
#Benescha Sinclair

import random

#Open a file
RandomFile = open("randomnumbers.txt", "w")

#Write 500 random numbers to the file.
for count in range(500):
    number = random.randint(1, 500)
    RandomFile.write(str(number) + "\n")

#Close the file
RandomFile.close()
print("Done")
