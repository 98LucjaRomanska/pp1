#unordered means that you cannot refer to an item by using an index
#dictionaries are ordered, changeable, and don't allow duplicates 

dicta = {
    'brand': 'Ferrari',
    'model': 'Testarossa',
    'year': 1984
}
x = dicta['year']
print(x)
#receiving new values
y = dicta.keys()
print(y)
#adding new items
dicta['color'] ='red'
print(y)
#getting a list of values
print(dicta.values())
#making changes in original dictionary
dicta['year']= 1996
print(dicta.values())
#get a list of key:value pairs
x = dicta.items() #results in tuple of list items
dicta['color']='blue'
print(x)
if 'model' in dicta:
    print('Yes, it is one of the keys')

#update dictionary
dicta = {
    'brand': 'Ferrari',
    'model': 'Testarossa',
    'year': 1984
}
x = dicta.items()
print(x)
dicta.update({'year': 2020})
print(dicta)

#removing items
dicta.pop('model')
print(dicta.items())
#remove the last inserted item
dicta.popitem()
print(dicta)
del dicta
#print(dicta) #here dicta is not defined

#empty the dictionary
dicta = {
    'brand': 'Ferrari',
    'model': 'Testarossa',
    'year': 1984
}
dicta.clear()
print(dicta)