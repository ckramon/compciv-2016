import requests
import os

os.makedirs('tempdata', exist_ok=True)

zname = os.path.join('tempdata', "ssa-babynames-nationwide-2014.txt")

mydict = []
with open(zname) as f:
    for line in f:
        name, sex, babies = line.strip().split(',')
        letter = name[-1]
        if mydict.get(letter):
            mydict[letter] += int(babies)
        else:
            mydict[letter] = int(babies)

for letter in string.ascii_lowercase:
    total = mydict[letter]
    print(mydict, ":", total)






