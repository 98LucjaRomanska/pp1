names =["Genowefa","Onufry","Celestyna","Alojzy","Pankracy"]
longest = 0
LN = ""
for row in names:
    for i in names:
        if len(row) >longest:
          longest = len(row)
          LN = row
          
        
print(longest)
sum="Names: "
for i in names:
   sum += i +" "
print(sum)
print(f'Longest name: {LN}')

print(type(len(row)))