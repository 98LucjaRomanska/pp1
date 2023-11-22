array = [2,3,2,5,8,1,9,8]
array.sort()
print(array)
a_string = []
for i in array:
    c = i + 1
    for c in array:
        if c!=i:
            a_string.append(i)
        elif c==i:
            pass
            

print(a_string)

    
