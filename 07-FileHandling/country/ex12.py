
name = "Anna May"
university = "Krakow University of Economics"
field = "Applied Informatics"

#write a file

file = open("student.txt", 'w')

print(file.write(name+"\n"))
print(file.write(university+"\n"))
print(file.write(field+"\n"))
file.close()