"""
x = "e e e e e"
print(len(x))
#n = input('Write sth: ')
# print(len(n))

print(x.split("e"))
print(type(x.split("e"))) #class list
print(len(x.split("e"))-1) #without "-1" it gives a value with empty spaces before and after the end of a sentence
# gives the number of letter "e" in sentence
"""
import ex23module
given_letter= 'e'
sen = 'You never get a second chance to make a first impression'
print(sen)
print(f'The number of letter "{given_letter}": {ex23module.count_character(sen, given_letter)}')

ex23module.count_character(sen, given_letter) 

#the function on its own does nothing
#it inicializes but it's hidden without 'print' statement

