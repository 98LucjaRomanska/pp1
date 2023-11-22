thistuple = ('a', 'b', 'c')
y = list(thistuple) 
print('list:',y)
y.append('d')
print(y)
thistuple= tuple(y)
print(thistuple)

#adding
thistuple2 = ('e',)
thistuple += thistuple2
print(thistuple)
#removing
y =list(thistuple)
y.remove('e')
thistuple = tuple(y)
print(thistuple)

#unpacking
fruits = ('apple','banana','mango','papaya', 'cherry')
(green, *tropic, red)= fruits
print(green)
print(tropic)
print(red)

#loop for a tuple 
print(fruits)
for x in fruits:
    print(x)
print("*"*40)
#loop through the index numbers
for x in range(len(fruits)):
    print(fruits[x])