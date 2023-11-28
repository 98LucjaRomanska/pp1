""" The sequence of digits contains the number of points rolled with a dice. Define a
function f(dice) that returns a number specifying the number of dice rolled the most
times in a row. Sample result:
"""
def f(dice):
    list=[]
    maximum = 1 
    for i in range(len(dice)):
        x =dice.split(dice[i]) # type(x)=list
        #print(x)
        list.append(len(x))
        
        if len(x)> maximum:
            maximum = int(dice[i])
        
    print(f'How many times this number occured in a string: {max(list)-1}') 
    print(f'The number of dice rolled the most time in a row: {maximum}')

print(f("2133"))
print(f("5233165554211"))