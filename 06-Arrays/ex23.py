
array = [-15,8,-31,-2,19]
max_number = 0
min_number = 0
for i in range(len(array)):
    if array[i]>max_number:
        max_number = array[i]
    else:
        pass
print(f'Maximum number: {max_number}')

for i in range(len(array)):
    if array[i]< min_number:
        min_number = array[i]
    else:
        pass
print(f'Minimum number: {min_number}')