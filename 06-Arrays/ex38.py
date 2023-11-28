n = int(input('Enter an integer: ')) #entered from the keyboard
arr = [7,8,2,5,-3] #given array
print(f'Given array: {arr}')
sum =" "
number = 0
for x in arr:
    if x > n:
        sum +=str(x)+ ' '
        number +=1
    else:
        pass
print(f'Elements greater than {n}: {sum}')
print(f'Number of elements greater than given n: {number}')


