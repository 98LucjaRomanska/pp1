from collections import deque

data =[1,2,3]
data.append(5)
#last in, first out: stack

print(data)
x = data.pop() #takes the last argument
print(data)
print(x)
#accesing last argument in a stack
print('The last argument:',data[len(data)-1])
print(" ")

#first in, first out: queue
data = [1,2,3]
data.append(4)
#look at the value which will be removed
print(data[0])
element = data.pop(0) #first argument pops out
print(element)
print(data)

data = deque()
print(data)
data.append('Caleb')
element = data.popleft() #==pop(0) used for first in, first out
print(element, data)