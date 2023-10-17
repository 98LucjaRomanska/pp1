import random
random.seed()
x = random.randint(1,6)
y = int(input('Guess the number from 1 to 6: '))
if y == x:
    print(True)
else:
    print(False)