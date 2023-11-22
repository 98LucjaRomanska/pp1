# a tuple
tuple = ('computation',)
print(type(tuple))
print(tuple)
#NOT a tuple
tuple =('computation')
print(type(tuple))
print(tuple)

#tuple = ('c','o','m','p','u','t','a','t','i','o','n')
#print(tuple)

#tuple
#ordered
#unchangeable- we cannot add or remove items after tuple was created
# since they are indexed they can have items with the same value
#can contain a different data types

#thistuple = tuple(("computation","kiwi")) 

#double-data brackets


#set
#set items are unchangeable (you cannot change its value)
#you can add or remove them
#unordered, unindexed
#no duplicate members 


#unhangeable = immutable


#update tuple
#conversion into list
x = ("apple",'banana','cherry')
y = list(x)
print(x)
print(y)
y[1]= "kiwi"
x = tuple(y)
print(x) #printing a tuple with changed element