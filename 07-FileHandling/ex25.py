import re
message = 'Tuesday: 22C, Wednesday: 21C, Thursday: 26C'
regex = r'\d\dC\b' 
arr = re.findall(regex, message)
print(arr)
#print(type(arr))
sum = 0
for row in arr:
    temp = int(row[0:2])
    sum +=temp
    print(temp)
average = int(sum/len(arr))
print(f'The average temperature: {average} C')


