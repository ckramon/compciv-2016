from os.path import join, basename
from csv import DictReader, DictWriter
DATA_DIR = 'data'
# DATA_FILE_NAME = join(DATA_DIR, '9-2011-fixed.csv')
DATA_FILE_NAME = join(DATA_DIR, '9-2014-fixed.csv')
WRANGLED_HEADERS = ['full_name', 'EMPLOYEE LAST NAME',  'EMPLOYEE FIRST NAME', 'EMPLOYEE RACE', 'EMPLOYEE GENDER', 'GENDER OF CONTACT', 'RACE OF CONTACT', 'TIME OF STOP']
WRANGLED_FILE_NAME = join(DATA_DIR, 'wrangled-data.csv')


# open the file 

with open(DATA_FILE_NAME, 'r') as thefile:
      original_rows = list(DictReader(thefile))



wrangled_rows = []
for row in original_rows:
    d = {}
    d['full_name'] = row['EMPLOYEE LAST NAME'] + ', ' + row['EMPLOYEE FIRST NAME']
    d['EMPLOYEE LAST NAME'] = row['EMPLOYEE LAST NAME']
    d['EMPLOYEE FIRST NAME'] = row['EMPLOYEE FIRST NAME'].strip()
    d['EMPLOYEE RACE'] = row['EMPLOYEE RACE']
    d['RACE OF CONTACT'] = row['RACE OF CONTACT']
    d['TIME OF STOP'] = row['TIME OF STOP']
    if row['GENDER'] is '1':
        d['EMPLOYEE GENDER'] = "M"
    elif row['GENDER'] is '2':     
        d['EMPLOYEE GENDER'] = "F"
    d['GENDER OF CONTACT'] = row['GENDER OF CONTACT']
    wrangled_rows.append(d)
    print(row['GENDER'], row['EMPLOYEE FIRST NAME'])
   
# write wrangled_rows into WRANGLED_FILE_NAME 

with open(WRANGLED_FILE_NAME, 'w') as thefile:
      c=DictWriter(thefile, fieldnames=WRANGLED_HEADERS)
      c.writeheader()
      for d in wrangled_rows:
        c.writerow(d)



