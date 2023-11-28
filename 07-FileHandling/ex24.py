import csv
import re
with open('students223.csv','r') as csv_file:
    csv_reader = csv.reader(csv_file)
    #reader function - what does it do
    regex = '\d\d'
    next(csv_reader)
    for line in csv_reader:
        #x = re.findall(regex, line)
      
        if int(line[2])<30:
            value = f'{line[0]}  {line[1]}  {line[-1]}'
            print(value)
        else:
            pass
"""
    with open('studentslist.txt','w') as new_file:
        csv_writer = csv.writer(new_file, delimiter = ' ') #it is a keyword
        for line in csv_file:
            csv_writer.writerow(line)
           

"""

