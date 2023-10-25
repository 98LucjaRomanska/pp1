current = float(input('Current product price: '))
previous = float(input('Previous product price: '))
reduction = 1 - current/previous

if 1 - current/previous > 0.1: 
    print('Buy the product!')
    print(f'Product price reduced by {int(reduction*100)}%')