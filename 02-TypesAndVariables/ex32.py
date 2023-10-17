x =float(input('Amount: '))
VAT= 0.23*x
string ='Amount: {:.2f}'
stringg= 'VAT 23%: {:.2f}'
print(string.format(x))
print(stringg.format(VAT))