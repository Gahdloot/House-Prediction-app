'''The idea of this script was to write a function that populates the database, then i tried importing the function into
 into the views page'''

with open('RentNew.csv') as f:

    lines = f.readlines()

for line in lines:
    a = line.rstrip('\n')
    veb = a.split(',')
    print(veb[0])


# for line in f:
    #     a = [line.rstrip('\n')]
    #     print(a