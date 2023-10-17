price = float(input('Enter price: '))
discount = float(input('Enter dicount %: '))
price_dis = price - price*0.01*discount
reduction = price - price_dis

x = "Price with discount: {:.2f}"
print(x.format(price_dis))

y = "Reduction: {:.2f}"
print(y.format(reduction))