import json
import os.path

zdir = os.path.join('tempdata', 'mapzen')
zname = os.path.join(zdir, 'stanford.json')

f = open(zname, 'r')
txt = f.read()
mydict = json.loads(txt)
f.close()

print("type:", mydict['type'])

query_dict = mydict['geocoding']['query']

print("text:" , query_dict['text'])
print("size:", query_dict['querySize'])
print("boundary.country:", query_dict['boundary.country'])





