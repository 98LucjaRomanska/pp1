import json
value ="""
{
    "title": "Tron:Legacy",
    "composer":"Daft Punk",
    "repease_year":2010,
    "budget":1700000,
    "actors":null, 
    "won_oscar":false, 
    "credits":{"director": "Andrew Niccol",
    "composer": "Michael Nyman",
    "cinematographer":"Sławomir Idziak"}
}"""
#load JSON data from a string
#json.loads(s)
tron = json.loads(value)
print(tron)

#output JSON object as a string
#json.dumps(j)
#it is not converted on python language
tr_output = json.dumps(tron, ensure_ascii=False)
print(tr_output)


