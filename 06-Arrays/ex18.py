arr =[
    [True,False],
    [True,True],
    [False,False]
]
x = 0
#mult = len(arr)*len(arr[0])
#print(mult)
for row in arr:
    for x in row:
        if x==True:
            row[x] = False
            
        elif x==False:
            row[x]= True
            
    print(row)
