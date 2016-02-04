import json
import os.path

zdir = os.path.join('tempdata', 'googlemaps')
zname = os.path.join(zdir, 'stanford.json')

f = open(zname, 'r')
txt = f.read()
f.close()

mydict = json.loads(txt)

for feature in mydict['features']:
    print(result['formatted_address'])