from collections import deque
queue = []
#first in, first out
#wsadzam na koniec ale biorę z początku
def push(val):
    queue.append(val)

def empty():
    return len(queue) == 0
def pop():
    if not empty():
        return queue.pop(0)
    else:
        return None
def display():
    for i in range(len(queue)-1,-1,-1):
        print(queue[i])
    print(queue)

if __name__=="__main__":
    que = [1,2]
    x = que.pop()
    print(x)
    display()
    

    