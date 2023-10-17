import math
circumference = float(input('Enter tree circumference: '))

#  y= 2*math.pi*r
r = circumference/(2*math.pi)

if r>= 50:
    r = True
else:
    r = False
print('Tree can be cut down: ', r)