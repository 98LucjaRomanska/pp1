arr1 = [2,4,5]
arr3 = [2,16,5]
arr4 = [45, 'juice']
arr2 = [2,3,4,5,6]
def subsetF(arr1, arr2):
    check =[]
    for x in arr1:
        for r in arr2:
            if x == r:
                compare = True
                check.append(True)
            else:
                compare = False
    print(check)
    if len(check)==len(arr1):
        subset = True
    else:
        subset = False
    return f'First array is a subset of second one: {subset}'

if __name__=="__main__":
    print(subsetF(arr1,arr2))
    print(subsetF(arr3,arr2))
    print(subsetF(arr4,arr2))
