

#f("1082") # 1+8=9 rem = 9%7=2 x=str(1082) if x[3]== rem: true
def f(product_code):
    sum = 0
    for i in range(len(product_code)-1):
        digit = int(product_code[i])
        sum +=digit
    #print(sum)
    rem = sum%7
    if int(product_code[3])==rem:   #bez int porównuje str z intem
        x = True
    else:
        x = False

    print(f"The fourth digit of p_code:{product_code[3]}")
    print(f"remainder: {rem}, {x}\n")
if __name__=="__main__":
    f("1082")
    f("2035")
    f("1114")
    f("7071")