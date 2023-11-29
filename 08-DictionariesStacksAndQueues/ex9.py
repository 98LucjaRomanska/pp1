countries = [
{"name":"Poland","population":38000000,},
{"name":"Germany","population":8900000,},
{"name":"France","population":1020000},
{"name":"Hungary","population":1330000}
]

i = 0
print(f'{"Country":10}{"Population":10}')
while i!=len(countries):
    print(f'{countries[i]["name"]:10} {countries[i]["population"]:10}')
    i += 1

