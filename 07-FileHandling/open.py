oceans = ['pacific','atlantic','indian']
with open('oceans.txt','w') as f:
    for ocean in oceans:
        f.write(ocean)
        f.write('\n')

    #python creates the file that's not exist
with open('oceans.txt','a') as f:
    print(23*"-",file = f)
    print("These are the 5 oceans.", file = f)


f = open('demofile.txt','r')
print(f.readline())
print(f.read(5))

#loop through the file line by line
f = open('demofile.txt','r')
for x in f:
    print(x)
f.close() #until i close the file changes will not appear
#remove the folder
#import os
#os.rmdir('myfolder')



