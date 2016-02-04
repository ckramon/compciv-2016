import requests
import os

os.makedirs('tempdata', exist_ok=True)

zname = os.path.join('tempdata', "ssa-babynames-nationwide-2014.txt")

malenum = 0
femalenum = 0

with open(zname) as text:
    for line in text:
        name, sex, babies = line.strip().split(',')
        if sex == 'F':
            if femalenum == 0:
                print("Top baby girl names")
            if femalenum < 5:
                femalenum += 1
                print(name, ":", babies)

        if sex == 'M':
            if malenum == 0:
                print("Top baby boy names")
            if malenum < 5:
                malenum += 1
                print(name, ":", babies)
