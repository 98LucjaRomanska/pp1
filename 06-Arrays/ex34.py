tup = (10,20,30,40,50)
#print(tup[-1])

i = -1
while tup[i]>tup[-len(tup)]:
    print(tup[i], end=" ")
    i -= 1
print(tup[0])
