n = [7,8,3,2,5]
def separate(arr):

    even =[]
    odd=[]
    for x in arr:
        if x%2 ==0:
            even.append(x)
        elif x%2 ==1:
             odd.append(x)
    combined = even + odd
    return combined
        
if __name__=="__main__":
    print(separate(n))