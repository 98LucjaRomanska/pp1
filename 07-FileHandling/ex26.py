import re
#number of vowels in the txt
txt ='To be, or not to be, that is the guestion'
regex = '[aeiuoy]'
x =re.findall(regex,txt)
print(x)
print(f'The number of vowels in the text: {len(x)}')
