inp = input('Enter Fahrenheit Temperature: ')
try: 
    fahr = float(inp)
    cel = (fahr - 32.0)*5.0/9.0
    print(cel)
except: 
    print('Please give a number: ')

# x = 1 y = 0
# x>= and (x/y)>2  
#python nie dochodzi do drugiego warunku jeśli pierwszy jest 0  #short-circut rule
#jeśli dochodzi bo x>= 2 to wyświetla error: division by zero 

#for is used to create repetition, range answers how many
#in each repetition number will have a different value
for number in range(3):
    print("An attempt", number + 1, (number + 1)*'.')

for number in range(1,4): #in the first iteration the first variable will be set to one
    print('An attempt', number)

for number in range(1,10,2):
    print('An attempt', number)
#nested loops
for x in range(5): #the outer loop
    for y in range(3): #the inner loop
        print(f"({x},{y})")

#range = a complex type 
#iterable 
for x in "python":
    print(x)
#a list is iterable
for x in [1,2,3,4]:
    print(x)
    break 
print('pause')

#for number in range(0,10, 2):
#    print(number)
count = 0
for number in range(1,10):
    if number%2==0:
        count=count + 1 #count+=1
        print(number)

print(f'We have {count} even numbers')







