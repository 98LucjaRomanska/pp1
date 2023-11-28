
f = open('ex21file.txt', 'w')
a_list = []
for x in range(1,51):
    a_list.append(str(x))
'''
delimiter=" "
a_string = delimiter.join(a_list)
print(a_string)
'''
for x in a_list:
    value = x+f'\n'
    f.write(value)
    
f.close()
f = open('ex21file.txt', 'r')
f.read()
f.close()
# the_list = [str(i) for i in range(1,5)]
