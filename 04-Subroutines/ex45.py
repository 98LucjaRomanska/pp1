def f(expression):
    a_string=""
    for c in range(len(expression)):
        a_string +=expression[c]+ " "

    list=[]
    list = a_string.split()
    
    sum = 0
    i = 0
    c = 1 

    while c<len(list):
        if list[c]=="-":
            while i<len(list): 
                an_integer = int(list[i])
                sum -= an_integer
                i +=2
            c += 2
        elif list[c]=="+":
             while i<len(list): 
                an_integer = int(list[i])
                sum =sum + an_integer
                i +=2

             c+=2
        
     
            
    print(sum)


f("2+3")
f("3+8+1")
f("3+8-1")