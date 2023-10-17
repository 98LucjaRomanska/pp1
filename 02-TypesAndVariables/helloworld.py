print("Hello World!")
print("Burbon wylał się na turban")
print("8888")
if 5>2:
    print("5 is greater than two")
#this is a comment
print("Hide me!") #It can be used at the end of 
#A value is created the moment you first assing a value to it.
"""
Variables do not need to be declared with any particular type, they can even change it
after they've been set.
"""
x = str(3)
y = int(3)
z = float(3)
print(x)
print(y)
print(z)

print(type(x)) #enables to get a type of a function
print(type(y))
print(type(z)) 
#x = y = z = "Świerszcz" print(x) print(y) print(z)

#creating an array
fruits = ["raspberry","blackberry", "strawberry"]
x, y, z = fruits
print(x)
print(y)
print(z)
#to output multiple variables use a comma or + operator
print(x, y, z)

x="python"
y = " is "
z = "awesome"

"""
print(x + y + z)
cc = 3
ct = "Jon"
print(cc + ct)    expect an error
"""
#using a global variable (a variable outside of a function)
x = "Narnia "

def myF():
    x="Fantasmagoria"
    global y 
    y = "Dragons"
    print(x + " is real") #local variable
    print(y + " are real")
myF()

print(x + "is ruled by Aslan") #outside of a function globalVr is still in use

#Datatypes
x = ["oxygen", "carbon", "hydrogen"]
print(x)
print(type(x))
y = ("oxygen", "carbon", "hydrogen")
print(y)
print(type(y))
x = range(7)
print(x)
print(type(x))

x = {"name": "Jeremy", "age": "67"}
print(x)
print(type(x))
y = ({"1","2","3"})
print(y)
print(type(y))
y = memoryview(bytes(67))
print(y)
print(type(y))

x = float(20.5)
y = bytes(5)
z = set(("violet","blue","green"))

print(x)
print(y)
print(z)

y = 15.56E4
print(y)
print(type(y))

#convert from float to int
x = 2.5
x = int(2.5)
print(x)
#convert from int to float 
y = 1
y = float(1)
print(y)
#convert from int to complex
z = 1
z = complex(1)
print(z)

#random module displays a random number from given range
import random
print(random.randrange(1,16))

x = str("s1")
y = str(34.66)
z = float("55")
a = float(77)

print(x, y, z, a)
a = '''Lorem ipsum dolor sit amet, consectetur adipiscing elit,
 sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.
   Ut enim ad minim veniam, quis nostrud exercitation ullamco 
   laboris nisi ut aliquip ex ea commodo consequat. Duis aute 
   irure dolor in reprehenderit in voluptate velit esse cillum
   dolore eu fugiat nulla pariatur. Excepteur sint occaecat 
   cupidatat non proident, sunt in culpa qui officia deserunt
   mollit anim id est laborum.'''
print(a)
print(len(a))

b = "Hello World!"
print(b[2])
#making a loop from a word
for x in "banana":
    print(x)

#len() returns the length of a string
y = "Hello, World!"
print(len(y))

#checking if word "fast-paced" is present in text
txt="You thrive in fast-paced environment"
print("fast-paced" in txt)

txt = "The best things in life are free"
if "free" in txt:
    print("Yes, it's free and present")

#check if 'expensive' is NOT in text
txt = "The best things in life are free"
print('expensive' not in txt)

txt = "The best things in life are free"
if "expensive" not in txt:
    print("No, expensive is NOT present. ")

x = "ż"
y = "aluzja"
print(x+y)

#slicing string
b = "Hello, World!"
print(b[2:12])
#slicing from the start/ the end
print(b[:5])
print(b[4:])
#negative indexes start from the end of the string
print(b[-5:-2])

#upper case
a = "Sachertort"
print(a.upper())
#lower case
b = "  Kalinka   "
print(b.lower())
#remove whitespace surrounding your actual text
print(b.strip())

#the replace() method replaces string with another string
a = "Yellow Submarine"
print(a.replace("Y", "H"))

print(a.split())
print(a.split('l'))
#merge a with b into variable c
a = "Hello"
b = "World"
c = a + " " + b
print(c)

quantity = 11
itemno = 23
price = 13.95
myorder = "I want {} pieces of item {} for {}."
print(myorder.format( quantity, itemno, price ))

#escape charakter
txt = "Winter and \"Petrol Company\" is coming"
print(txt)
#carriage return
txt = "Hello\rWorld"
print(txt)

width = 17
height = 12.0
print(width)
print(type(width))

print(height)
print(type(height))

width = float(width)
print(width)
print(type(width))

mod = width//2 
print(mod)
print(type(mod))

dv = width/2.0
print(dv)
print(type(dv))

dvh =height/3
print(dvh)
print(type(dvh))

x = 1 + 2*5 
print(x)

#celsius = input('please give me Celsius')
#x = input(celsius)


#boolean expressions
#not (x > y) #not is true when x>y is false: x must be less than or equal to y
#x is y #x is the same as y
#x is not y #x is not the same as y
# x > 0 and x < 10 #koniunkcja, oba warunki muszą być spełnione

n =int(input("Enter number: "))
if n<10:
    print('n is less than 10')
else: 
    print('n is greater than 10.')






