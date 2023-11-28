def f(sentence):
    sentence.split()
    # print(sentence.split())
    list = sentence.split()
    a_string=""
    for c in range(len(list)):
        a_string +=list[c]
    print(a_string)
        
    
if __name__=="__main__":
    f(" A computer is weak")
