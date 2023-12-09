arr = [[0,0,0,0,0],
       [0,0,0,0,0],
       [0,0,0,0,0],
       [0,0,0,0,0],
       [0,0,0,0,0]]

c = 1
for row in arr:
    row = [i*c for i in range(1,6)]
    print(row)
    c +=1
    
"""
arr2 = [i for i in range(2,12,2)]
arr3 = [i for i in range(3,16,3)]
arr4 = [i for i in range(4,21,4)]
arr5 = [i for i in range(5,26,5)]
"""
