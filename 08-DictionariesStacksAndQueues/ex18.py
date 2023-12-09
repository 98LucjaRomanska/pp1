import json
import ex17
def function():
    for key, value in ex17.ICAO.items():
        print(key, value)

icao_file = open("icao_file.txt","w",encoding = "utf-8")

done = json.dump(ex17.ICAO,icao_file, indent = 4, sort_keys= False,separators =(" "," "), skipkeys= True)
#separators - formats the output 
#separators (",",": ")
print(done)
icao_file.close()

#another method
placement = open('place.txt','w')
for key, value in ex17.ICAO.items():
    
    placement.write(f' {key.upper()} {value}\n')
placement.close()
