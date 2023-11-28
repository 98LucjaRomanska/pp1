g = open('ex23file.txt','w')

for x in range(1,11):
    first = x
    second = x**2
    third = x**3
    value = f'{first}, {second}, {third}\n'
    g.write(value)
g.close()