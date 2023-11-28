def f(vnum):                        #i give an integer
    number=str(vnum)                #convert it to a string
    a_string=""
    for c in range(len(number)):
        a_string += number[c] + " "

    new_list= a_string.split()
    print(new_list)


def ff(num):
    list=[]
    number =str(num)
    for c in range(len(number)):
        list.append(int(number[c]))
    print(list)
    list.sort()
    print(list)
    sum = 0
    for i in range(len(number)):
        if list[i]==list[i+1]:  #wrong
           sum =list[i]+list[i+1] 
    print(sum)




ff(3034)
f(4034)
