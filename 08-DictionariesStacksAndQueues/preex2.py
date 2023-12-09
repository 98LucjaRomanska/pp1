car ={
    'brand':'Ferrari',
    'model':'Testarossa',
    'year': 1984
}
#returns values
for x in car:
    print(car[x])

#return the keys
for x in car.keys():
    print(x)

#loop through key:value pairs
for x, y in car.items():
    print(x,y) 

#copy dictionary
mydict =dict(car)
print(mydict)

#nested dictionaries
child1 = {
    'name': 'Mordechaj',
    'age': 19
}
child2 = {
    'name': 'Błażej',
    'age': 21
}
child3 = {
    'name': 'Anna',
    'age': 34,
}
myfamily ={
    'child1': child1,
    'child2': child2,
    'child3': child3
}
#accesing the nested 
print(myfamily['child2']['age'])