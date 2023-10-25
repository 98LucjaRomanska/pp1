x = input('Enter EAN-13 article number: ')
if len(x)== 13 and x[:3]=="590":
    print('Article number is correct')
    print('Article manufacturered in Poland')
elif len(x) == 13:
    print('Article number is correct')
    