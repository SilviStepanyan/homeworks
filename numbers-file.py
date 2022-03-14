import random

f = open("numbers.txt", "w")

len1 = 1000000000

while len1:
    f.write(str(random.randrange(0, 121)))
    f.write(',')
    len1 = len1 - 1

f.close()
