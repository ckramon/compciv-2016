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
    loc = result['geometry']['location']
    mylist.append(str(loc['lng']))
    mylist.append(str(loc['lat']))
        
print(';'.join(mylist))