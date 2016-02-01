import requests
import os

os.makedirs('tempdata/googlemaps', exist_ok=True)
os.makedirs('tempdata/mapzen', exist_ok=True)


zipurl = 'http://www.compciv.org/files/datadumps/apis/googlemaps/geocode-stanford.json'
print("Downloading:", zipurl)
resp = requests.get(zipurl)
zdir = os.path.join('tempdata', 'googlemaps')
zname = os.path.join(zdir, 'stanford.json') 
print("Writing file:", zname)
zfile = open(zname, 'w')
zfile.write(resp.text)
zfile.close()
# ok counting things
line_num = resp.text.count("\n")
char_count = len(resp.text)
print(zname, "has", line_num, "lines and", char_count, "characters")


#########################

zipurl = 'http://www.compciv.org/files/datadumps/apis/mapzen/search-stanford.json'
print("Downloading:", zipurl)
resp = requests.get(zipurl)

zdir = os.path.join('tempdata', 'mapzen')
zname = os.path.join(zdir, 'stanford.json') 
print("Writing file:", zname)

zfile = open(zname, 'w')
zfile.write(resp.text)
zfile.close()

line_num = resp.text.count("\n")
char_count = len(resp.text)

print(zname, "has", line_num, "lines and", char_count, "characters")
