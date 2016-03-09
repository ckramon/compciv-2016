from os.path import join, basename
from glob import glob
DATA_DIR = 'tempdata'

tally = {'M': set(), 'F': set()}

for fname in glob(join(DATA_DIR, '*.txt')):
    # doing the filtering if filenames in one loop
    year = basename(fname)[3:7]
    if year >= "1950":
        for line in open(fname, 'r'):
            name, gender, babies = line.split(',')
            tally[gender].add(name)

# alltxtfiles_path = join(DATA_DIR, '*.txt')
# alltxtfiles_names = glob(alltxtfiles_path)

# a_filename = 'tempdata/yob1951.txt'
# bname = basename(a_filename)

# year = bname[3:7]

# myfilenames = []
# for fname in alltxtfiles_names:
#   bname = basename(fname) # e.g. "yob1980.txt"
#   year = bname[3:7]       # e.g.    "1980"
#   if year >= "1950":
#       myfilenames.append(fname)

# totalsdict = {'M': 0, 'F': 0}

# for fname in myfilenames:
#     babyfile = open(fname, "r")
#     for line in babyfile:
#         name, gender, babies = line.split(',')
#         # need to convert babies to a number before adding
#         totalsdict[gender] += int(babies)

print("F:",len(tally['F']), "M:",len(tally['M']))
# print("F/M name ratio:" len(tally['F'])/len(tally['M'])

# print("F:", str(tally['F']).rjust(6),
#       "M:", str(tally['M']).rjust(6))


f_to_m_ratio = round(100 * len(tally['F']) / len(tally['M']))
print("baby ratio:", f_to_m_ratio)