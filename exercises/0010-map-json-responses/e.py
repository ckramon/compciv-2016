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
    mylist.append(c['formatted_address'])
    for c in result['geometry']:
        mylist.append(c['lng'])
        mylist.append(c['lat'])
        mylist.append(str['location'])
        
      
    print(';'.join(mylist))