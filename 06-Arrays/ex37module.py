arr_n = [7,2,8,5,2]
def numbers(arr):
    sum=""
    for x in arr:
        sum +=str(x)+' '
    return f'Numbers: {sum}'
        

na_pozniej = max(arr_n)
print(na_pozniej)
def second(arr):
    arr2 = arr
    arr2.remove(max(arr2))
    return f'Second largest element: {max(arr2)}'
    


def differ(arr):
    arr.append(na_pozniej)
    difference = max(arr) - min(arr)
    return f'difference:{difference}'

#print(differ(arr_n))


def median(arr):
    arr2= arr
    arr2.sort()
    return arr2


''' 
def median(arr):      
    arr2 = arr
    sum =0
    for x in arr:
        sum += x

    q = int(sum/2)
    mod = sum%2

    if mod==1:    
        median = q + mod
    
    elif mod == 0:
        median = q
    
    return f'Median: {median}' 
'''

#print(median(arr_n))    

def d(arr):
    new =[min(arr),max(arr)]
    return f'Smallest and largest numbers: {new}'
#print(d(arr_n))

def string(arr):
    sum = " "
    

    for c in range(len(arr)):
        if arr[c]< arr[-1]:
           sum +=str(arr[c])+"-"
        elif arr[c]==arr[-1]:
            sum +=str(arr[-1])
    return f'Numbers as a string: {sum}'

#print(string(arr_n))


if __name__=="__main__":
    print(numbers(arr_n))
    print(second(arr_n))
    print(median(arr_n))
    print(d(arr_n))
    print(string(arr_n))
    print(differ(arr_n))

