data = [2,3,4,5]
x = sum(list(map(lambda n: n**2, data)))
#list konwertuje wyniki z map do listy
#sum sumuje mi zawartość tablicy


data = [15.90, 38.47, 4.07, 132.70, 9.15]
x = round(sum(list(map(lambda n: n*4.5, data))))
print('Sum of transactions:', x)