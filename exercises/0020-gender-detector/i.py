from os.path import join
import csv
DATA_DIR = 'tempdata'
WRANGLED_DATA_FILENAME = join(DATA_DIR, 'wrangled2014.csv')


rfile = open(WRANGLED_DATA_FILENAME, 'r')
datarows = list(csv.DictReader(rfile)) # just make it all a big list of dicts

# because numbers in a CSV file are deserialized/importated
# as plain strings, we need to do some work to re typecast them
# to integers
for r in datarows:
    r['total'] = int(r['total'])
    r['males'] = int(r['males'])
    r['females'] = int(r['females'])
    r['ratio'] = int(r['ratio'])
    # these operations *mutate* the r object, thus
    # every object in datarows has been transformed...but that's cool

bigdatarows = []
for row in datarows:
    if r['total'] > 99:
        bigdatarows.append(row)

print("Popular names with a gender ratio bias of less than or equal to:")
for genderratio in (60, 70, 80, 90, 99):
    print(" ", genderratio,"%:", r['total'], "/", len(bigdatarows))