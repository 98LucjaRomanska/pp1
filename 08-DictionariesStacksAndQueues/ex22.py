stack = []
#add value at the top of the stack
def push(value):
    stack.append(value)
#return true if the stack is empty
def empty():
    return len(stack) == 0


def pop():
    if not empty():
        return stack.pop()
    else:
        return None
    
def display():
    x = -1
    for i in range(len(stack)-1,-1, x):
        print(stack[i])
    print(stack)
    
if __name__=="__main__":
    push(3)
    display()