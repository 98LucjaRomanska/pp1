txt = 'For only {price: .2f} dollars!'
print(txt.format(price = 49))
#get the first character of the string
x=txt[0]
print(x)
y = txt[2:5]
print(y)
txt = "Hello World!"
z = txt.upper()
print(z)
txt= txt.replace("H","J")
print(txt)
#{} : placeholder for given parameter
#comparing two values, the expression is evaluated and python returns the boolean answer
print(46666<=599)
#print a mess on whether a condition is true or false
a = input("number one:")
b = input("number two:")
if b>a:
   print("b is greater than a")
else:
   print('a is greater than b')
#True- False statements
x = "Sobota"
print(bool(x))
print(bool([]))
print(bool(None))
#function that returns a boolean value
def MyF():
   return False
print(MyF())
#check whether an object is an integer or not
x = 400
print('Does this object is a float number?')
print(isinstance(x, float))
print('This object comes under ', type(x))

txt ="Hello World!"
x =txt[0:2]
print(x)