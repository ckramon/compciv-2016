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
    for c in result['formatted_address']:
        mylist.append(c['long_name'])
    print(';'.join(mylist))

    