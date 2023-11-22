arr_n = [10,20,30,40,50]

def second(arr):
    arr.remove(max(arr))
    return max(arr)
print(second(arr_n))

arr_n.append(50)

def differ(arr):
    difference = max(arr) - min(arr)
    return difference

print(differ(arr_n))
print(arr_n)

#popraw differ()


def median(arr):       
    arr.sort()
    q = int(len(arr_n)/2)
    mod = len(arr_n)%2

    if mod==1:    
        median = q + mod
    
    elif mod == 0:
        median = len(arr_n)/2
    
    return median

print(median(arr_n))    

def d(arr):
    new =[min(arr),max(arr)]
    return new
print(d(arr_n))

def string(arr):
    sum = " "
    

    for c in range(len(arr)):
        if arr[c]< arr[-1]:
           sum +=str(arr[c])+"-"
        elif arr[c]==arr[-1]:
            sum +=str(arr[-1])
    return sum

print(string(arr_n))




