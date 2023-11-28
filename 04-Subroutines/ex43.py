
def f(txt):
    list=txt.split()
    print(list)
    len(list)
    i =0
    something =""
    while i<len(list):
        something +=list[i][0]
        i +=1

    print(something)

if __name__=="__main__":
    f("That's your shit")
    f("python")
    f("don't you want me Baby don't you want me ooooooo")