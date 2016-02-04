import requests
import os

os.makedirs('tempdata', exist_ok=True)

zname = os.path.join('tempdata', "ssa-babynames-nationwide-2014.txt")

allmalebabies = 0
allfemalebabies = 0


# with open(zname) as f:
#     for line in f:
#         name, sex, babies = line.strip().split(',')
#         if sex == 'M':
#             allmalebabies = int(babies) + allmalebabies

#         if sex == 'F':
#              allfemalebabies = int(babies) + allfemalebabies
mydict = requests.loads(txt)
for line in fileobject:
    name, sex, babies = line.strip().split(',')
    last_letter = name[-1]
    if mydict.get(last_letter):
        mydict[last_letter] += int(babies)
    else:
        mydict[last_letter] = int(babies)


print(last_letter, ":", int(babies))






