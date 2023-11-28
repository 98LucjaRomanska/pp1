def f(n):
    remainder = 1
    while remainder != 0:
        quo = int(n/5) # 23/5 = 4 r.3
        remainder = n - quo*5 #  23 - 4*5= 3 
        coin5 =quo
        n = remainder #3
        quo = int(n/2)
        remainder = n - quo*2 # 3 - 1*2 = 1
        coin2 =quo
        n = remainder #1
        quo = int(n/1)
        remainder = n - quo*1
        coin1 = quo

        sum = coin5 + coin2 + coin1
    
    return sum

if __name__=="__main__":
    print(f(23))
    print(f(8))
    print(f(0))
    