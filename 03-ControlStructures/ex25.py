purchased = int(input('Number of products purchased: '))
price = int(input('Product price: '))
reduction = 0.25

if purchased <= 2:
    total_pay = purchased * price
    print(total_pay)
else:
    total_pay = 2*price + (1 - reduction)*price*(purchased - 2)
    print("Amount to pay: ", total_pay)
