import random
x = random.randint(1,6)
print('Dice rolled: ', x)
if x == 1 or x==6:
    x =True
else: 
    x = False
print('Special number: ', x)