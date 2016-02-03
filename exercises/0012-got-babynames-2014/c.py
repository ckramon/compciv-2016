import requests
import os

os.makedirs('tempdata', exist_ok=True)

zname = os.path.join('tempdata', "ssa-babynames-nationwide-2014.txt")

ka = da = 0

with open(zname) as z:
    for line in z:
        name, sex, babies = line.strip().split(',')
        if sex == 'F':
            if name == 'Daenerys':
                da += int(babies)
            elif 'Khaless' in name or 'Khalees' in name:
                ka += int(babies)

print('Daenerys:', da)
print('Khaleesi:', ka)