import re
txt = "The rain in Spain"
x =re.search('^The.*Spain$', txt)
if x:
    print("YES! We have a match!")
else:
    print('No match')

#return a list containing every occurence of 'ai'
x = re.findall('ai',txt)
print(x)