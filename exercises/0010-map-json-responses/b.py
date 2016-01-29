import json
f = open(stanford.json, 'r')
txt = f.read()
f.close()

mydict = json.loads(txt)

