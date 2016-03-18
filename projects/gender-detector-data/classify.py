from os.path import join
from csv import DictReader, DictWriter
from gender import detect_gender
DATA_DIR = 'data'
CLASSIFIED_DATA_HEADERS = ['full_name', 'EMPLOYEE LAST NAME',  'EMPLOYEE FIRST NAME', 'EMPLOYEE RACE', 
'EMPLOYEE GENDER',  'gender', 'ratio', 'usable_name', 'GENDER OF CONTACT', 'RACE OF CONTACT', 'TIME OF STOP']

WRANGLED_FILE_NAME = join(DATA_DIR, 'wrangled-data.csv')
CLASSIFIED_DATA_FILENAME = join(DATA_DIR, 'classified-data.csv')


def extract_usable_name(namestr):
    return namestr

# Set up the new data file
w = open(CLASSIFIED_DATA_FILENAME, 'w')
dw = DictWriter(w, fieldnames=CLASSIFIED_DATA_HEADERS)
dw.writeheader()

# Open the non-gender classified data file
with open(WRANGLED_FILE_NAME) as r:
    datarows = list(DictReader(r))
    # read each row
    ct = 0
    for row in datarows:
        usablename = extract_usable_name(row['EMPLOYEE FIRST NAME'])
        ct += 1
        print("Row:", ct, "extracting --", usablename, "-- from:", row['EMPLOYEE FIRST NAME'])
        gender_result = detect_gender(usablename)
        # now add usable_name and gender data to each row
        row['usable_name'] = usablename
        row['gender'] = gender_result['gender']
        row['ratio'] = gender_result['ratio']
        dw.writerow(row)