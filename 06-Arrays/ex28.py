def compare(arr1, arr2):
    for c in arr1:
        for i in arr2:
            if c==i:
                print(c, i)




#arr1=[True, False]
#arr2=[True,False,True]

#arr1 =[5,3,1]
#arr2 = [5,3,1]
#arr1 = [3,2,1]
#arr2 = [3,2]

def compare(arr1,arr2):
    a_string2= ' '
    a_string1 = ' '

    for z in arr2:
        a_string2 += str(z) + ' '
    for t in arr1:
        a_string1 += str(t) + ' '

    for c in range(len(arr1)):
        for i in range(len(arr2)):
            if c == i and len(arr1)==len(arr2):
                if arr1[c]==arr2[i]:
                    x = True
                elif arr1[c]!=arr2[i]:
                    x = False
                    break
            else:
                    x = False

    if x==True:
        n= 'arrays are the same'
    else:
        n = 'arrays are not the same'

    return f'Array1: {a_string1}', f'Array2: {a_string2}', f'Comparison: {n}'

if __name__=="__main__":
    print(compare(['water','book','sky'],['water','book','sky']))
    print(compare([True, False],[True,False,True]))
    print(compare([5,3,1],[5,3,1]))
    print(compare([3,2,1],[3,2]))
            



#compare(["water",'book','sky'],['water',#'book','sky'])