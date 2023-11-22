arr1 = [4,36,12,28,9,44,5]
arr2 = [5,1,36]
arr3 = []
for c in arr1:
    for i in arr2:
        if c== i:
            arr3.append(c)
        else: 
            pass
print(arr3)       
for c in arr1:
    for i in arr3:
        if c==i:
            arr1.remove(c)

print(arr1)



            

