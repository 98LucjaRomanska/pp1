arr=[2,3,7,5,4]
print(arr)
print("number of elements: ",len(arr))
print(arr[0]) #first value
print(arr[1])
print(arr[-1])
#print(len(arr[len(arr[])-1]))
print(arr[4]) #last but one value
print(arr[len(arr)-2])

print(type(arr[0]))
sum = arr[0]+arr[-1]
print(sum)

#middle value

print(f'middle value: {arr[len(arr)//2]}')


#średnia arytmetyczna
sum= 0
for n in arr:
    sum+=n
print(sum)
print(sum/len(arr))

#loop statement
for i in arr:
    print(i, " ", end=" ")

i=0
while i<len(arr)//2:
    print(arr[i]," ", end=" ")
    i+=1