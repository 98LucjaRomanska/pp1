#x = input('Enter the PIN code: ')
# print(x[:4])

for i in range(1, 4):
    x = input('Enter the PIN code: ')
    if x[:4]=="0805":
        print("Payment accepted")
        break
    else:
        print("Incorrect...")
    i += 1
else: 
    print('Sorry, your payment card has been blocked')
        
