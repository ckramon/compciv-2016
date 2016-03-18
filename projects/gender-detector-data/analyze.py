from os.path import join
from csv import DictReader, DictWriter
from gender import detect_gender
DATA_DIR = 'data'

CLASSIFIED_DATA_FILENAME = join(DATA_DIR, 'classified-data.csv')

all_rows = list(DictReader(open(CLASSIFIED_DATA_FILENAME)))

unique_officers = {}
for d in all_rows:
    name = (d['full_name'], d['gender'], d['EMPLOYEE GENDER'])
    if unique_officers.get(name):
        unique_officers[name] += 1
    else:
        unique_officers[name] = 1


# gender detected gender

male_count = 0
female_count = 0
for o in unique_officers.keys():
    o_gender = o[1]
    
    if o_gender == 'M':
        male_count += 1
    
    elif o_gender == 'F':
        female_count += 1



print("There are", male_count, "males")
print("There are", female_count, "females")
print(male_count/female_count)

# actual listed gender

male_count = 0
female_count = 0
for o in unique_officers.keys():
    o_gender = o[2]
    
    if o_gender == 'M':
        male_count += 1
    
    elif o_gender == 'F':
        female_count += 1



print("There are", male_count, "males")
print("There are", female_count, "females")
print(male_count/female_count)

# gender of offenders



###

from collections import defaultdict

# male_cop_tally = {'M': 0, 'F': 0}
# female_cop_tally = {'M': 0, 'F': 0}

male_cop_tally = defaultdict(int)
female_cop_tally = defaultdict(int)


for row in all_rows:
    cop_gender = row['EMPLOYEE GENDER']
    stopped_gender = row['GENDER OF CONTACT']

    if cop_gender == 'M':
        male_cop_tally[stopped_gender] += 1
    elif cop_gender == 'F':
        female_cop_tally[stopped_gender] +=1
print(male_cop_tally) 
print(female_cop_tally)

male_gender_ratio = (male_cop_tally['M'] + 1) / (male_cop_tally['F'] + 1)
female_gender_ratio = (female_cop_tally['M'] + 1) / (female_cop_tally['F'] + 1)

print(male_gender_ratio)
print(female_gender_ratio)

male_cop_tally = defaultdict(int)
female_cop_tally = defaultdict(int)


for row in all_rows:
    cop_gender = row['EMPLOYEE GENDER']
    stopped_race = row['RACE OF CONTACT']
    if cop_gender == 'M':
        male_cop_tally[stopped_race] += 1
    elif cop_gender == 'F':
        female_cop_tally[stopped_race] +=1


print(male_cop_tally) 
print(female_cop_tally)

male_cop_tally = defaultdict(int)
female_cop_tally = defaultdict(int)


for row in all_rows:
    cop_gender = row['EMPLOYEE GENDER']
    stop_time = row['TIME OF STOP']
    if cop_gender == 'M':
        male_cop_tally[stop_time] += 1
    elif cop_gender == 'F':
        female_cop_tally[stop_time] +=1


print(male_cop_tally) 
print(female_cop_tally)

# male_gender_ratio = (male_cop_tally['M'] + 1) / (male_cop_tally['F'] + 1)
# female_gender_ratio = (female_cop_tally['M'] + 1) / (female_cop_tally['F'] + 1)

# male_count = 0
# female_count = 0
# for o in unique_officers.keys():
#     o_gender = o[4]
    
#     if o_gender == 'M':
#         male_count += 1
    
#     elif o_gender == 'F':
#         female_count += 1



# print("There are", male_count, "males")
# print("There are", female_count, "females")
# print(male_count/female_count)

# gender ratio of officers to offenders



# genderdict = {'M': [], 'F': []}
# for gid, person in unique_officers.items():
#     gd = person['GENDER']
#     genderdict[gd].append(person)



# genderdict = {'M': [], 'F': []}
# for gid, person in unique_officers.items():
#     gd = person['GENDER']
#     genderdict[gd].append(person)

# unique_officer_count = len(unique_officers)

# # look at the ratio of female to male officers involved in highway stops in Washington
# for gd in ['F', 'M']:
#     gendered_officers = genderdict[gd]
#     print("For traffic stops in the state of Washington, the estimated gender breakdown for officers is:")
# for gd in ['F', 'M']:
#     gendered_officers = genderdict[gd]
#     ratio = round(100 * len(gendered_officers)/unique_officer_count)
#     print("\t" + gd + ':', len(gendered_officers), str(ratio) + '%')
    
# #     counted_gender = []
# #     for row in datarows:
# #         d = {}
# #         ct += 1
# #         print("Gender:", row['GENDER'], ct)

# # look at the ratio of female to male non white officers involved in highway stops in Washington        

# with open(CLASSIFIED_DATA_FILENAME) as r:
#     datarows = list(DictReader(r))
    
#     ct = 0
#     for row in datarows:
#         gender = extract_usable_name(row['EMPLOYEE RACE'])
#         ct += 1
#         print("Row:", ct, gender, ['EMPLOYEE RACE'])
       


# # look at the ratio of female officers to female offenders in Washington 

# # look at the ratio of female officers to male offenders in Washington 

# # look at the ratio of male officers to male offenders in Washington 

# # look at the ratio of male officers to female offenders in Washington 
   

