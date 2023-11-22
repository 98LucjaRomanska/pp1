arr = [12,6,4,9,10]
def star(n):
    for i in arr:
        n = i*"*"
        print(f'{i}: {n}')

star(arr)