'''
binary = "110a1"
deconcatenate = " "
len(binary)
for c in range(len(binary)):
    deconcatenate += binary[c] + " "
print(deconcatenate)

print(deconcatenate.split())   
'''
binary = "01a"
print(binary)
a_string =""
for c in range(len(binary)):
    if binary[c] =="1" or "0":  #if a charakter is 1 and 0 (in conjunction) then it is put to a_string
        a_string += binary[c]  
        x = True
    elif binary[c] != "1" and"0":
        print("It's not binary number")
        x = False
        break
print(x)



    


"""
def f(binary_number):
    if "0"and "1" in binary_number:
        print(True)
    else:
        print(False) #this program shows whether 0 and 1, both are present in the string
        # a0134gg is ok for its function
    
f(binary)
"""