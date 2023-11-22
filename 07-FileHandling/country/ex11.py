file =open('numbers.txt','r')
counter = 0
for line in file:
    counter +=int(line)
    print(line, end="")
    print()
    print(f'Sum: {counter}')
    file.close()

    #pliki są, czekają na kolokwium jako dane do odczytu