

person ={
    "basic_data" : {
    "name":"Barbara",
    "age": 21
    },
    "advanced_data" : {
    "status": "student",
    "married": False,
    "interest": ["reading","swimming"]
    }
}

for dictionary_id, inf in person.items():
    print(f'ID of dictionary: {dictionary_id}')
    for key in inf:
        print(key, ":", inf[key])