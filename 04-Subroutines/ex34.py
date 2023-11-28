def f(n):
    i = 0
    a_string=""
    while i<n:
        i+=1
        a_string += str(i)
    print(a_string)

if __name__=="__main__":
    f(11)
    f(4)