#lambda/anonymous functions don't have any name
# lambda is a keyword that says what follows is an anonymous funtction
#you can give it a name
g = lambda x: 3*x + 1
#title() - only first charakter is capitalized
#strip() - removes whitespaces
def build_quadratic(a, b , c):
    return lambda x: a*x**2 + b*x + c

print(build_quadratic(3,0,1)(2)) #build quadratic function and pass the second value, evaluated for x = 2
#the expression is 3*x**2 + 1 now
#lambda functions are good only for once

def cm(feet= 0, inches = 0):
    inches_cm = inches * 2.54
    feet_cm = feet*12*2.54
    return inches_cm, feet_cm

def bmi(kg, cm):
    x = kg//(cm*0.01)**2
    return lambda x: x 
 #print(f'Peter lambda is {bmi(81,182)}')

x = bmi(81, 182)
print(f'Peter lambda is {x}')

