import json
import os.path

zdir = os.path.join('tempdata', 'mapzen')
zname = os.path.join(zdir, 'stanford.json')

f = open(zname, 'r')
txt = f.read()
mydict = json.loads(txt)
f.close()

print("type:", mydict['type'])

for i in mydict['geocoding']:
    mylist = []
    mylist.append(i['query'])
    loc = i['geocoding']['query']
    mylist.append(str(loc['text']))
    mylist.append(str(loc['size']))
    mylist.append(str(loc['boundary.country']))

print(';'.join(mylist))

# print("text:", mydict['geocoding']['query'])



# for result in mydict['results']:
#     mylist = []
#     mylist.append(result['formatted_address'])
#     loc = result['geometry']['location']
#     mylist.append(str(loc['lng']))
#     mylist.append(str(loc['lat']))

# for i in mydict['geocoding']:
#     mylist = []
#     mylist.append(str(i['text']))
#     mylist.append(str(i['size']))
#     mylist.append(str(i['boundary.country']))
        
# print(';'.join(mylist))
        
# print("type:", mydict['type'])
# print("text:" , mydict['text'])
# print("size:", mydict['querySize'])
# print("boundary.country:", mydict['boundary.country'])