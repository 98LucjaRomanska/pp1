#zadanie 16
#exponentiation
x = 2**10
print(x)
#square root
squareroot = 49**(1/2)
print(squareroot)
#procent of sth
procent = 1/4 * 80
print(procent)
#zadanie 17
x = 4 + 4/2**2
print(x)
x = 4%3%2%1
print("The remainder of expression 4 %3 %2 %1 is ", x)
#bool operators
y = True!= False
print("Is True different than False?: ",y)
y =2<=3 or False
print("Is it true that 2 is smaller or equal to 3?", y)
#boolean type 
z = 2<3 and 4<5 or 7<6 #koniunkcja i alternatywa
#alternatywa jest (1) gdy co najmniej jeden z warunków zostanie spełniony
#dlatego ostatecznie true
print(z)
z = 2%3<4/5 and 6+7<8 or not 9+10 == 19
print(z)
#18
x = 7
y = 34
print('Value of x:',x)
print('Value of y:',y)
z = x #7
x = y #34
y = z #7
print('Value x after swapping: ', x)
print('Value y after swapping: ', y)
#19
a = 4
print('Cube side: ', a)
print('Cube volume: ', a**3)
print('Cube surface area: ', a**2*6)
#20
num_one = int(17)
num_two = int(5)
print('Number one:', num_one)
print('Number two: ', num_two)
print('Division result: ', int(num_one/num_two))
print('Remainder: ', num_one%num_two)
#21
"""
age = 45
months = 3
x = "I have {} years old and {} months."
print(x.format(age, months))
"""
cent = 160
feet = cent*0.033
inch = cent*2.54
print("Measurements in feet", feet)
print("Measurements in inches", inch)
x = "I am {0} tall, i.e. {1} feet and {2} inches."
print(x.format(cent, feet, inch))

#22
a = 3
b = 5
x = a - b
expression= '{0}-{1}={2}'
print(expression.format(a,b,x))
#23
a = int(input('Enter a: '))
b = int(input('Enter b: '))
c = int(input('Enter c: '))
p = 1/2*(a+b+c)
circumference ='Triangle circumference: '
print(circumference, 2*p)

P = (p*(p-a)*(p-b)*(p-c))**(1/2)
print('Triangle area: ', P)





