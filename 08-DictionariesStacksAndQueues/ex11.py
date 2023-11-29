import json
movie = {
    "title": "ADC",
    "year": 1986,
    "actor":{"leading":"Jo Jo","suporting":"No No"},
    "length": "2min",
    "interesting":"yes"
}
file = open('favourite.json',"w")

json.dump(movie, file, indent = 6)
file.close()

#codewars