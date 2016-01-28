import os
a = open(os.path.join("tempdata", "tragedies", "hamlet"), 'r')

for x in range(5):
    print(a.readline().strip())


a.close()

