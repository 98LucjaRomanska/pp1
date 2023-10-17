#testing random
import random
random.seed()#it will always be the same for the same given value
print('A random float number between 0 and 1: ',random.random())

print('A random integer: ',random.randint(1,6))
#returns a number bwtween 1 and 6 (both are included)
print('A random integer: ', random.randrange(1,7))
#returns a number betwwen 1(included) and 7(not included)
import random
#print("Three dice rolls: ", random.randrange(1,7),", ",random.randrange(1,7),", ",random.randrange(1,7))
x = random.randrange(1,7)

y = random.randrange(1,7)

z = random.randrange(1,7)
print("Three dice rolls: ", x, ", ", y, ", ", z)
print("The sum of dice rolled: ", x + y + z)

import math
print(math.pi)

x = int(input("Enter a number from 1 to 10: "))
if 0 < x: 
    if x < 10:
        print('Given value is a positive single-digit number')

