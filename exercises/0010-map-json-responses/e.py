import json
import os.path

zdir = os.path.join('tempdata', 'googlemaps')
zname = os.path.join(zdir, 'stanford.json')

f = open(zname, 'r')
txt = f.read()
f.close()

mydict = json.loads(txt)

for result in mydict['results']:
    mylist = []
    mylist.append(result['formatted_address'])
    for c in result['geometry']:
        for c in result['location']:
            mylist.append(str(result['lng']))
            mylist.append(str(result['lat']))
        
print(';'.join(mylist))