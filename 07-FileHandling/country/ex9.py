file = open('countries.txt','r')
#file_content = file.read()
#print(file_content)

#display text line
counter = 0
for line in file:
    counter += int(line)
    print(f'{counter}. {line}', end= " ")

file.close()