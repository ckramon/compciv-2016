from os.path import join, basename

START_YEAR = 1950
END_YEAR = 2015
DATA_DIR = 'tempdata'

for year in range(START_YEAR, END_YEAR, 5):

    names_dict = {}
    thefilename = join(DATA_DIR, 'yob' + str(year) + '.txt')
    thefile =  open(thefilename, 'r')
    for line in thefile:
        name, gender, count = line.split(',')
        if not names_dict.get(name):
            names_dict[name] = {'M': 0, 'F': 0}
        names_dict[name][gender] += int(count)

    thefile.close()



    total_namecount = len(names_dict.keys())


    total_babycount = 0
    for v in names_dict.values():
        totes = v['M'] + v['F'] 
        total_babycount += totes


    print(year)

    print("Total:", round(total_babycount / total_namecount), 'babies per name')


    for gd in ['M', 'F']:
        babycount = 0
        namecount = 0
        for v in names_dict.values():
            if v[gd] > 0:
                babycount += v[gd]
                namecount += 1
        print("    %s:" % gd, round(babycount / namecount), 'babies per name')



    