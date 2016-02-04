import requests
import os

os.makedirs('tempdata', exist_ok=True)

zname = os.path.join('tempdata', "ssa-babynames-nationwide-2014.txt")

m_dict = {}
f_dict = {}

with open(zname) as text:
    for line in text:
        name, sex, babies = line.strip().split(',')
        letter = name[-1]
        if sex == 'F':
            if f_dict.get(letter):
                f_dict[letter] += int(babies)
            else:
                f_dict[letter] = int(babies)
        else:
            if m_dict.get(letter):
                m_dict[letter] += int(babies)
            else:
                m_dict[letter] = int(babies) 
print("letter","F".rjust(10,''), "M".rjust(7,'')) 
print("------------------------")

for letter in string.ascii_lowercase:
    female=str[f_dict(letter)]
    male=str[m_dict(letter)]

print(letter, female.rjust(15,''), letter, male.rjust(7,''))



        #         print("Top baby girl names")
        #     if femalenum < 5:
        #         femalenum += 1
        #         print(name, ":", babies)

        # if sex == 'M':
        #     if malenum == 0:
        #         print("Top baby boy names")
        #     if malenum < 5:
        #         malenum += 1
        #         print(name, ":", babies)