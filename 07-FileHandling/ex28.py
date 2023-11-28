import re
q = open('sample1.txt','r')
regex ='\w\w\w\w\w\w+'
count = 0
for line in q:
    count += 1
    print(' ')
    print(f'line: {count}')
    x = re.findall(regex, line) #x= array
    for i in range(len(x)):
        print(x[i])
    
    

q.close()