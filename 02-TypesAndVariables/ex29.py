#returns a number betwwen 1(included) and 7(not included)
import random
#print("Three dice rolls: ", random.randrange(1,7),", ",random.randrange(1,7),", ",random.randrange(1,7))
x = random.randrange(1,7)

y = random.randrange(1,7)

z = random.randrange(1,7)
print("Three dice rolls: ", x, ", ", y, ", ", z)
print("The sum of dice rolled: ", x + y + z)