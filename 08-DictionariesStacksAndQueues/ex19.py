import json
first = open('students.json','r')
done = open('limited.json','w')

json_file = open('students.json','r', encoding='utf-8')
#load JSON data from a file
#json,load(f)
per = json.load(json_file) #big list containing dictionaries, which have py syntax
#print(per) #converted to python syntax
#print(per)
limited = open('limited.json','w')
i = 0
while i<10:
    push = json.dumps(per[i]["name"])
    print(push) #wypchałam składnię pythona do pliku json
    i += 1
i = 0 
for row in per: #per is a list
    if i> 10:
        break
    else:
        new_list = [{row["name"],row["surname"], row['student_ID']}]
        for x in new_list: #row is a dict
           print(f'{x} : {x.values()}') 
    i += 1

    
"""
while i < 100:
    limited.write(f'{personal[i]["name"]} {personal[i]["surname"]}  {personal[i]["student_ID"]}')
    i += 1
"""

  

done.close()
json_file.close()