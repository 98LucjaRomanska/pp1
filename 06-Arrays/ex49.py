array = [[-38,19],
       [5,40],
       [-7,11],
       [29,16]]

def maxi(arr):
    maxi = 0
    index = 0
    c = 0
    holder = [index, c]
    for row in arr:
        c = 0
        for i in row:
            if i>maxi:
                maxi = i
                holder[0] = index
                holder[1] = c
            elif i < maxi:
                pass
            c += 1
        index +=1
    return f'The maximum number: {maxi}\nCoordinates of the location: {holder}'
def mini(arr):
    mini = 0
    index = 0
    c = 0
    holder = [index,c]

    for row in arr:
        c = 0
        for i in row:
            if i<mini:
                mini = i
                holder[0] = index
                holder[1] = c

            elif i < mini:
                pass
            c += 1
        index += 1
    return f'The minimum number: {mini}\nCoordinates of the location: {holder}'

if __name__=="__main__":
    print(mini(array))
    print(maxi(array))

    