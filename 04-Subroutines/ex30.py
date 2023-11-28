
'''
a_string= " "
print("The lenght:", len(number))

for c in range(len(number)):
    a_string +=number[c] + " "

print(a_string.strip())               #removes whitespaces at the beginning and the end
print(a_string.split())

print("the break")
'''
def f(number, EVEN):
    list=[]
    for c in range(len(number)):
        list.append(int(number[c]))

    print(list)
    
    odd = []
    even =[]
    for c in range(len(number)):
        num = int(number[c])  
        if num%2 == 0:
            even.append(num)
        elif num%2 ==1:
            odd.append(num)
            
    sum = 0
    if EVEN == True:
        for i in range(len(even)):
            sum +=even[i]
    else:
        for i in range(len(odd)):
            sum +=odd[i]
            
    print(sum)

if __name__=="__main__":
    f("3124",True)
    f("3124",False)
    f("20576",False)
    f("20576",True)





