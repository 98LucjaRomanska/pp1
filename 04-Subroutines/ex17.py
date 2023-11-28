def different(n1, n2, n3):
    if n1 != n2 != n3: 
        return True
        # print(f'Numbers {n1}, {n2} and  {n3} are different')
    else:
        return False

a = input("Enter first number: ")
b = input("Enter second number: ")
c = input("Enter third number: ")
print(a)
print(b)
print(c)

if different(a,b,c):  
    print(f'Numbers {a}, {b} and {c} are different')
else:
    print('False')


# 2

def different(n1,n2,n3):
    return True

if different(3,4,5):
    print('Numbers are different')
else:
    print('Some of them are the same')