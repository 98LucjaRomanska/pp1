n ='An apple a day keeps a doctor away'
zero = ' '
nostalgic = "How long, how long will I slide? Separate my side, I don't I don't believe it's bad. Slit my throat, it's all I ever…"

def a2(a_string):
    array = a_string.split()
    #print(array)
    if len(array)==1:
        for x in array[0]:
            if x ==' ':
                mess  = None
            else:
                mess = len(array)
            return mess
    elif len(array)!=1:
        return f'Number of words: {len(array)}'

# print(a2(n))
#print(a2(zero))
#print(a2(nostalgic))
# print(len(zero))



def ordered(a_string):
    arr = a_string.split()
#by creating a function
    def length(e):
        return len(e)
    arr.sort(reverse =True, key =     length)
    return f'Words from the longest: {arr}'


def c(a_string):
    arr = a_string.split()
    arr.sort()
    return f'Words ordered alphabeticllay: {arr}'

def auxS(a_string):
    sum =""
    array = a_string.split()
    for row in array:
        print(row,end=',')
  
    return sum

if __name__=="__main__":
    print(f'Text: {n}')
    print(a2(n))
    print(ordered(n))
    print(c(n))
    print(auxS(n))




            



