f = open('output1.txt','r')
count = 0
for x in f:
    count = count + 1
    print(f'{count}. {x}')
    if count%5==0: 
        n = input("Press 'Enter' to continue. ")
        print(n)
        if (True):
            continue
    
        
    