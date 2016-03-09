import requests
import os

os.makedirs('tempdata', exist_ok=True)

zname = os.path.join('tempdata', "ssa-babynames-nationwide-2014.txt")

zipurl = 'http://stash.compciv.org/ssa_baby_names/ssa-babynames-nationwide-2014.txt'
resp = requests.get(zipurl)
mytext=resp.text

records_list = []
lines = open(ssa-babynames-nationwide-2014.txt, 'r').readlines()
for line in lines:
    name, sex, babies = line.strip().split(',')
    row = [name, sex, int(babies)]
    records_list.append(row)

def foo(babies):
    return float(babies['mag'])

sortedbabies = sorted(lines, key=foo, reverse=True)[0:5]


print()