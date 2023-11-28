
x = 19
y = 23
if lambda x, y: x!=y:
    if x > y:
        print(True)
    else:
        print(False)
#lambda is a keyword that says, what follows is an anonymous function


#this anonymous function has 2 inputs
full_name= lambda fn,ln: fn.strip().title() + " " + ln.strip().title()
print(full_name('SaySheShe','Bombons'))


#sort(key = lambda ) is a function

list = ['Isaac Asimov', 'Ray Radbury', 'Arthur C. Clarke', "Michał Abecedowski"]
list.sort(key = lambda name: name.split(" ")[-1].lower())
print(list)


x = int(input("Enter a number: "))
y = int(input("Enter a number: "))
#x = 19
#y = 23
if lambda x, y: x != y:
    if x > y:
        print(True)
    else:
        print(False)
#lambda is a keyword that says, what follows is an anonymous function