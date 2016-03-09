import requests
import os

os.makedirs('tempdata', exist_ok=True)

zname = os.path.join('tempdata', "ssa-babynames-nationwide-2014.txt")

zipurl = 'http://stash.compciv.org/ssa_baby_names/ssa-babynames-nationwide-2014.txt'
resp = requests.get(zipurl)
mytext=resp.text

namesdict = {}

with open(zname) as f:
    for line in f:
        name, sex, babies = line.strip().split(',')
        if namesdict.get(name):
            namesdict[name] += int(babies)
        else:
            namesdict[name] = int(babies)