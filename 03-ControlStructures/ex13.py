number1 =str(input('Enter first number:'))
number2 = str(input('Enter second number: '))
if number1[0]!="-" or number2[0]!="-":
    print(f'Ate least one of the number {number1} and {number2} is not negative')


number1 =int(input('Enter first number:'))
number2 =int(input('Enter second number: '))
if number1>=0 or number2>=0: 
    print(f'At least one of the number {number1} and {number2} is not negative')