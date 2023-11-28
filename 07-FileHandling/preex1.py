import re
names = ['Finn   Binderballe',
         'Geir Anders Berge',
         'HappyCodingRobot',
         "Ron      Weasley",
         'Son!c']
regex = '^\w+\s+\w+$'
# starts with a random number of ch., one or more whitespaces, ends with a random number of ch.

for name in names:
    result = re.search(regex, name)
    if result:
        print(name)
        #print(result)

#search for word char sequence starting with a C
regex = 'C\w*'
#word starting with a C, followed by zero or any ch.
for name in names:
    match = re.search(regex, name)
    if match: 
        print(name)
        #print(match.start())
        print(match.span())
        print(match.group())
print(" ")

regex = '^(?P<first_name>\w+)\s+(?P<last_name>\w+)$'
#we group and gain access by () method
for name in names: 
    match = re.search(regex, name)
    if match:
        print(match.group('first_name'))#^(\w+)
        print(match.group('last_name'))#(\w+)$

#we can create our custom character set
regex = '^[a-zA-Z!]+$'
for name in names:
    if re.search(regex,name):
        print(name)

#scan for blocks of lower case letters
regex = '[a-z]+'
for name in names:
    matches = re.findall(regex,name)
    if matches:
        print(matches)

regex = '[a-z]+'
for name in names:
    matches = re.finditer(regex,name)
    #access to the match object 
    for match in matches:
        print(match)

values = ['https://www.socratica.com',
          'https://www.socratica.com/collections',
          'zgerypala',
          'halo dzbanie']

regex = 'https?'
for value in values:
    if re.match(regex,value):
        #match f scans txt for a match
        print(value)
regex = 'https?://w{3}.\w+.(org|com)'
for value in values:
    if re.fullmatch(regex,value):
        print(value)
        #strings that fully match the regex



    
