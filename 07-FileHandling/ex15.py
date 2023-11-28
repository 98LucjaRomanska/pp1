with open('guido.txt','r') as alternative_way:
    bio = alternative_way.read()
#with 'with' technique I do not need to close the file/ It is already done. 

for line in bio: 
    print(line, end="")
