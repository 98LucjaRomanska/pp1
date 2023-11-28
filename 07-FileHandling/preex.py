import re #Regular Expressions
txt = "Co trzeba? Trzeba napisać podanie, a do podania dołączyć życiorys"

x = re.findall('podani',txt)
print(x)
#Check if the string starts with ...
x =re.findall('\ACo',txt)
print(x)
x =re.findall(r'\bCo',txt)
print(x)
#a match if characters are at the end
x = re.findall(r'życiorys\b',txt)
print(x)
x = re.findall('życiorys\Z',txt)
print(x)
#a match if a string contains any word characters
x =re.findall('\w',txt)
print(x)
#a match if a string DOES NOT contain any word characters
x = re.findall('\W',txt)
print(x)
if x: print('A match')
else: print('No match')

n = ['Francois', 'Mike','Nick']
x = re.findall('^\w\w\w\w',n)
print(x)