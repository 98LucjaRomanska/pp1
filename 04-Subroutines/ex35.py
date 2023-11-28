def f(number1, number2, operator):
    if operator=="+":
        result= number1 + number2
    elif operator == "-":
        result =number1 - number2
    elif operator =="*":
        result =number1*number2
    elif operator =="%":
        result =number1%number2
    elif operator =="**":
        result =number1**number2
    print(f'f({number1},{number2},"{operator}") returns {result}')

if __name__=="__main__":
    f(2,3,"*")
    f(2,3,"**")
    f(2,3,"-")