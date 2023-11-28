import re
q = open('ex29file.txt','r')
regex = '\d.\d'
sum = 0
for char in q:
    x = re.findall(regex,char)
    if len(x)>0:
        print(x)
        for element in x:
            sum += float(element)
        mean = sum/len(x)
        print(f'{sum} / {len(x)} = {str(mean)[:6]}')
        print(f"The arithmetic mean of Peter's grades: {str(mean)[:6]}")

    else:
        pass

q.close()
