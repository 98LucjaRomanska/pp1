stack =[]
n = '2 3 + ='
n = '2 4 1 + * ='
n = '2 3 + 4 5 + * ='
n = '8 3 1 + / 3 2 - 4 + * ='
a_list = []
control = ['0','1','2','3','4','5','6','7','8','9']

for x in n:
    if x!=" ":
        a_list.append(x)
    else:
        pass
#index of an element in a_list

for x in range(len(a_list)):
    for num in control:
        if a_list[x]==num:
            a_list[x] = int(a_list[x])
        else:
            pass
            
print(a_list)
i = 0
for i in range(len(a_list)):
    x = a_list[i]
    if type(x)==int:
        stack.append(x)
    else:
        if x=='+':
            first = stack.pop()
            sec = stack.pop()
            sum = first + sec
            #print(sum)
            stack.append(sum)
            print(stack)
        elif x=='-':
            first = stack.pop()
            sec = stack.pop()
            sub = first - sec
            stack.append(sub)
        elif x=='/':
            first = stack.pop()
            sec = stack.pop()
            div = first/sec
            stack.append(div)
        elif x=='*':
                first = stack.pop()
                sec = stack.pop()
                mul = first*sec
                stack.append(mul)

        elif x=='=':
            print(stack)


if __name__=="__main__":
    n = '2 3 + ='
    n = '2 4 1 + * ='
    n = '2 3 + 4 5 + * ='
    n = '8 3 1 + / 3 2 - 4 + * ='



