person = {
    "name": "Marek",
    "surname": "Banach",
    "age": 25,
    "hobby": ["swimming","excursions"],
    "married": True,
    "phone":{"landline":"123444321","mobile":"777888999"}
   }
print(person)
print(person["name"])
print(person["hobby"][1]) #to jest tablica, wybieram index
person["surname"]="Nowak"
person["married"]= not person["married"]
person["gender"]='male' #klucz:wartość zostają dodane
person["hobby"] +=['bicycle']
person['phone']['work']="123456789" #phone -słownik>nowy klucz
print(person)