arr =[
    [1,3,5],
    [8,7,2]
]
#a 
sum= arr[0][0] + arr[-1][-1]
print("Sum of the first element in the first row and the last element in the last row: ", sum)
#b
sum=0
for i in range(len(arr)):
    sum += arr[i][len(arr)//2]
print("Sum of the elements in the middle column: ",sum)
#c
sum= 0
for i in range(len(arr[0])):
    sum+=arr[-1][i]
print("Sum of the elements in the last row:", sum)

