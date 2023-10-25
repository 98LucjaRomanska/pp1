washing_product = input('Choose a washing product (shoes/underwear/jacket): ')
shoes = 20 
underwear = 70
jacket = 40
if washing_product =="shoes":
    washing_product = 20
elif washing_product=="underwear":
    washing_product= 70
elif washing_product == "jacket":
    washing_product = 40
print(washing_product)
print(type(washing_product))

rinse =int(input("Rinse? 15 minutes (0/1) "))

if rinse== 0:
    rinse = False
elif rinse== 1:
    rinse = True
print("rinse =", rinse)

if rinse == True: 
    rinse = 15
elif rinse == False:
    rinse = 0



spin = int(input("Spin? 9 minutes (0/1) "))

if spin == 0:
    spin = False
elif spin == 1:
    spin = True
print("spin =", spin)

if spin == True:
    spin = 9
    print(spin)
elif spin == False:
    spin = 0

total_time = washing_product + rinse + spin 
print(f"Total washing time: {total_time} minutes")









    
    
