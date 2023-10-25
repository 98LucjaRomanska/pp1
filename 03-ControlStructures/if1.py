
age = int(input('Enter your age: '))
if age>=18 and age< 100:
    print('You are signed up!')
elif age>= 100:
    print('You are too old to sign up!')
elif age<18 and age>0:
    print('You are too young to sign up.')
else:
    print('You are not born yet!')

name = input('Enter your name: ')
if name =="":
    print("You did not type your name")
else:
    print(f"Hello {name}. Nice to meet you.")

online = True
if online:
    print('You are online.')
else:
    print('You are not online.')

    