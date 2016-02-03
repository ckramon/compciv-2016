import requests
import os

os.makedirs('tempdata', exist_ok=True)

zname = os.path.join('tempdata', "ssa-babynames-nationwide-2014.txt")

babies = 0

with open(zname) as f:
    for line in f:
        babies += int(line.split(',')[2])

print("There are", babies, "babies whose names were recorded in 2014")
