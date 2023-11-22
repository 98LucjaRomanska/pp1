import random
arr1=[3,7,1,0,4]
print(arr1)
print(" ")
arr2=[[2,3],[7,1],[0,4]]
for row in arr2:
    print(row)

print(" ")
arr3=[]
for i in range(5):
    arr3.append(7)
print(arr3)
#d
arr4 =[]
for i in range(1,10):
    arr4.append(i)
print(arr4)

arr4= [i for i in range(1,10)]
print("This is arr4: ", arr4)
#e
arr5 = []
for i in range(1,10):
    arr5.append(i*2)
print(arr5)

arr5=[i*2 for i in range(1,10)]
print(f"This is arr5 {arr5}")

#f
arr6 = []
for i in range(10):
    arr6.append(random.randint(1,20))
print(arr6)
arr6=[random.randint(1,20) for i in range(10)]
print(f"This is arr6 {arr6}")
#g
arr7 = []
for i in range(5):
    arr7.append([])
print(arr7)

arr7=[[] for i in range(5)]
print(f'This is arr7: {arr7}')
#h
arr8 = [[1 for i in range(2)] for j in range(4)]
print(arr8)       
#i
arr9 = [[random.randint(1,20) for i in range(3)] for j in range(5)]
print(f'This is arr9 {arr9}') #5 segments with 3 columns within

#j
array = [4,0,3]
print(array)
#k
arr =[0 for i in range(15)]
print(f'15-elements, 0 within :{arr}')
#l
arr = [random.randint(1,31) for i in range(30)]
print(arr)
print("The length of an array: ",len(arr))

#m 
m = [random.randint(0,1) for i in range(20)]
print(m)
#n
n = [[False for i in range(2)] for j in range(5)]
for j in range(5):
    print(n[j])