def f(text):
    list = []
    if len(text)>1:
        for i in range(len(text)-1):
            list.append(text[i])
            list.append("-")
        list.append(text[len(text)-1])
        print(list)
        print("".join(list))
    else:
        print(text)
    
    

if __name__=="__main__":
    f("University")
    f("UE")
    f("x")
    f("")