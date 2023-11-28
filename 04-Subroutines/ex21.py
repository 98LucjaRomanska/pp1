import mymath
import mykeyboard
x = int(input("Enter a number: "))
y = mymath.generate_number()
print("Computer number:", y)

print( type(mymath.generate_number()))


if x != y:
    
    print('Nice try, try again')
else:
    print('You won the game!')