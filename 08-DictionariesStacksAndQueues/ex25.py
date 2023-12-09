#program that calculates the RPN expressions
n ='2 4 1 + * ='
a_list = []
numbers = ['0','1','2','3','4','5','6','7','8','9']

l2= []
#make an RPN first
for x in n:
    if x ==" ":
        pass
    elif x!=' ':
        for num in numbers:
            if num==x:
                a_list.append(int(x))
            else:
                continue
print(a_list)

for x in a_list:
    while x  in numbers:           
        el = a_list.pop()
        el2 =a_list.pop()
        print(el)
        print(el2)

    if x=="+":
            expression = el+ el2
            a_list.append(expression)
    elif x=="/":
            expression = el/el2
            a_list.append(expression)
    elif x=='*':
            expression = el*el2
            a_list.append(expression)
    elif x=='-':
            expression = el - el2
            a_list.append(expression)
    elif x=="=":
        print(expression)
 




            


"""
print(a_string)
for i in range(len(a_string)):
    if type(a_string[i]) is int :
        print(True)
    else:
        print(False)
"""