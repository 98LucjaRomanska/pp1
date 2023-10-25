PLN = int(input("Enter the amount in PLN: "))
#we have only 1, 2 and 5 Polish Zlotys in coins
"""
coin5 = PLN%5
coin2 = (PLN - 5*coin5)%2
coin1 = (PLN - 5*coin5 - 2*coin2)
print(f'The amount of PLN {PLN} in coins: ')
print("5 coins:", coin5)
print("2 coins:", coin2)
print("1 zloty coin:", coin1)
"""

print(f'The amount of PLN {PLN} in coins: ')
coin5 = int(PLN/5)
print("5 zl -", coin5)
coin2 = int((PLN - 5*coin5)/2)
print("2 zl -", coin2)
coin1 = int((PLN - 5*coin5 - 2*coin2)/1)
print("1 zl -", coin1)
