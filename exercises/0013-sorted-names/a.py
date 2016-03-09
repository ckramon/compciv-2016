import requests
import os

os.makedirs('tempdata', exist_ok=True)

zname = os.path.join('tempdata', "ssa-babynames-nationwide-2014.txt")

zipurl = 'http://stash.compciv.org/ssa_baby_names/ssa-babynames-nationwide-2014.txt'
resp = requests.get(zipurl)
mytext=resp.text


zfile = open(zname, 'w')
zfile.write(mytext)
zfile.close()

char_count = len(resp.text)

print("There are", char_count, "characters in tempdata/ssa-babynames-nationwide-2014.txt")