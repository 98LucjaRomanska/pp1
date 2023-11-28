import json
json_file = open('sample2.json','r', encoding='utf-8')
#load JSON data from a file
personal = json.load(json_file)
json_file.close()
print(personal)
print(type(personal))
print(personal['gender'])
print(personal['address'])
#load JSON data from a string
#json.loads(s)

#write JSON object to file
#json.dump(j,f)
#output JSON object as a string
#json.dumps(j)
