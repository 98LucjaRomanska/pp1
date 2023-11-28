import ex45 
dimensional = [ 7,3,7,9,0,
                2,9,0,1,5,
                3,8,6,4,7,
                8,7,1,1,5 ]
#ex45.dimen2x4(dimensional)
for x in range(len(dimensional)):
    if x%5 == 0 and x>0:
        print(dimensional[x])
    else:
        print(dimensional[x], end='')

# print(dimensional[0], end=' ')
x = 0
while len(dimensional)>x> 0:
    if x%5 == 0:
        print(x)
    else:
        print(x, end=' ')
    
    x += 1 

    