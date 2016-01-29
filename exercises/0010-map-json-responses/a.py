import requests
import os

os.makedirs('googlemaps')

zipurl = 'http://www.compciv.org/files/datadumps/apis/googlemaps/geocode-stanford.json'

print("Downloading: http://www.compciv.org/files/datadumps/apis/googlemaps/geocode-stanford.json")
resp = requests.get(zipurl)

zname = os.path.join('googlemaps','stanford.json') 
zfile = open(zname, 'w')
zfile.write(resp.text)
zfile.close()

print("Writing file: tempdata/googlemaps/stanford.json")

fname = os.path.join('googlemaps', 'stanford.json')
googlemapsfile = open(fname, 'r')
line_num = 0
for x in googlemapsfile:
    line_num += 1
def count_letters(word, char):
    count = 0
    while count <= len(word):
        for char in word:
            if char == word[count]:
                count += 1
            return count

googlemapsfile.close()

print(fname, "has", line_num, "lines and", count_letters "characters")

import requests
import os

os.makedirs('mapzen')

zipurl = 'http://www.compciv.org/files/datadumps/apis/mapzen/search-stanford.json'

print("Downloading: http://www.compciv.org/files/datadumps/apis/mapzen/search-stanford.json")
resp = requests.get(zipurl)

zname = os.path.join('mapzen', 'stanford.json') 
zfile = open(zname, 'w')
zfile.write(resp.text)
zfile.close()

print("Writing file: tempdata/mapzen/stanford.json")

fname = os.path.join('mapzen', 'stanford.json')
mapzenfile = open(fname, 'r')
line_num = 0
for x in mapzenfile:
    line_num += 1
mapzenfile.close()

print(fname, "has", line_num, "lines and", char_count "characters")
