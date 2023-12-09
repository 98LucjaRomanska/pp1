import random
arr = []

c = 1
while c <=5:
        row = [i*c for i in range(1,4)]
        arr.append(row)
        print(row)
        c+=1

print(" ")
first_row = arr.pop(0) # the first
last_row = arr.pop() #the last

print(arr)
arr.insert(0,last_row)
arr.append(first_row)
print(arr)





