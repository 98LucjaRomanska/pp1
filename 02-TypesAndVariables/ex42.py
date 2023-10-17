binary = input('Enter binary number: ')
print(binary)
count = -1
print(type(count))
for x in binary:
    count+=1
    print("A value of binary digit", x,": ", 2**count*x)
    position = 2**count
    y = int(x)
    print(position, position*y)

    

