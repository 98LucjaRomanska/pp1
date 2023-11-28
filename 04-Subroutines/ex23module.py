#a program (subroutine) that calculates how many times a given letter appears in any text

def count_character(x, l):  #l= a given letter  x= a given string
    
    # print(len(x.split(l))-1)
    the_list = len(x.split(l))-1
    return the_list




if __name__=="__main__":
    l = "e"
    x ='volunteering'
    print(count_character(x, l))