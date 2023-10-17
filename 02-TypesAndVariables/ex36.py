x = float(input("Bank buys EUR: "))
y = float(input('Bank sells EUR: '))
spread = y - x
writing = 'Spread: {:.4f}'
print(writing.format(spread))