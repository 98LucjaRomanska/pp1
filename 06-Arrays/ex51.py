arr = []
c = 1
while c <=5:
        row = [i*c for i in range(1,4)]
        arr.append(row)
        print(row)
        c+=1
print(' ')
for row in arr:
    last = row[-1]
    first= row[0]
    row[0]= last
    row[-1]= first 
    print(row)
        
