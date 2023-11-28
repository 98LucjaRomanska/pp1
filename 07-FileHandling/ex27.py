import re
text = 'To be, or not to be, that is the question'
regex = '\s'
x = re.split(regex,text)
print(x)
print(f'The number of words: {len(x)}')
