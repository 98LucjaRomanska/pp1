stack = []

n = int(input('Enter natural number:'))
while n > 0:
    div = int(n/2)
    rem = n%2
    stack.append(rem)
    n = div
else:
    stack.reverse()
    sum = ""
    for x in stack:
        sum += str(x)
    print(sum)


