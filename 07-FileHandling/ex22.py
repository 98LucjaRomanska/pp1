import random
g = open('ex22file.txt','a')

array = [random.randint(100,999) for i in range(50)]
for x in array:
    g.write(str(x) + f'\n')
g.close()