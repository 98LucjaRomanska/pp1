name = input('File name: ')


f = open(name, 'r')
# I don't read()
count = 1
for line in name:
    count += 1
print("Number of lines:", count)

