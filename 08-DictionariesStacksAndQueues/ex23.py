import ex22 as stack
ast = [] #a_stack
#a
stack.display()
#b,c,d
stack.push(2)
stack.push(14)
stack.push(9)
#e
stack.display()
#f
element = stack.pop()
print('Get element from the stack:',element)
stack.display()
#h
stack.push(31)
stack.push(6)
stack.display()
#k
el = stack.pop() #arg 0
el2 = stack.pop()# arg 1
print(el, el2)
#l
stack.display()
