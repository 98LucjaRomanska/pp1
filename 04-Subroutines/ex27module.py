def f(n):
    x = n[0:2]
    asterisk = n[2:12]
    z = n[-4: ]
    asterisk ="*"*10

    
    return x + asterisk + z
   
if __name__=="__main__":
    print(f('4444333322221111'))