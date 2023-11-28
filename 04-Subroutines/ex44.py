def f(password):
    a_string=""
    for i in range(len(password)):
        a_string += password[i]+ " "
    print(a_string)
    list = a_string.split()
    print(list)
    print(sorted(password))
    alfabetic = sorted(password)
    for i in range(len(password)):
        pass

f("malinka")    
