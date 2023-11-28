import math
x = 27
st = 1
for i in range(2,int(math.sqrt(x))+ 1):
    if x/i==0:
        st = 0
        print('Not prime')
        break
    else:
        if st == 1:
            print('Prime')
            print(st) 

#jak to zrobić !!!!!

