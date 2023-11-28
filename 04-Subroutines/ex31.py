def negative(x,y):
    i = x 
    c = 0
    while i >=x and i<=y:

        if i%2 == 0 and i < 0:
            c +=1
        i = i + 1
    return f'f({x},{y}) returns {c}'

if __name__=="__main__":
    print(negative(-7,5))
    print(negative(-1,11))
    