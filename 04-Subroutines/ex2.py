#a
import math
x = math.log(5)
print(x)
#my own
z = math.fabs(-5)
print(int(z))
# b : exponentiation
x = math.exp(3) # return e raised to the power x 
print(x)
# math.exp2(x)
x = math.exp2(3) # returns 2 raised to the power x 
print(x)
# c 
square_root = math.sqrt(7)
print(square_root)
# d
sine = math.radians(90)
print("Convert the angle x from degrees to radians: ", sine)
sine = math.sin(90)
print("Return the sine of x radians: ", sine)

#without a paretheses python gives the memory address of function f()

def ping(): #f without any arguments
    return "Ping!"
def volume(r):  #r will be required argument
    #returns the volume of a sphere with radius r.
    v = (4.0/3.0)* math.pi * r**3
    return v
print(volume(3))

def cm(feet = 0, inches = 0):  # default arguments, which need a beginning value right now
    inches_to_cm = inches * 2.54
    feet_to_cm =feet * 12 * 2.54
    return inches_to_cm, feet_to_cm 

feet = input("feet")
inches = input("inches")
print(cm(feet, inches))


def g(y, x = 0): # without defining an y it comes as an 'required argument'
    pass