def check_within(number, x, y):
    x < y
    if number >= x and number<= y:
        return "yes"
    else:
        return "no"
    
if __name__=="__main__":
    number = 7
    x = 2
    y = 15
    print(check_within(number,x,y))