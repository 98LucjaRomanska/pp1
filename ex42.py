print("7", "8", "9")
print("4", "5", "6")
print("1", "2", "3")
# for i in range(-6,-1, -3):
#        print(f'{i} = {i}', end=" ")
"""
for i in range(-6, 1):
    i= i*(-2)
    for j in range(1,4):
        print(f'{i} + {j} = {i+j}', end=' ')
    print()
"""
i = -6
j = 1
while i >= -6 and i <= 1:
    n = i*(-2)
    #i = i*(-1)
    i = i + 1
    while j <= 4 and j >= 1:
        print(f'{n} + {j} = {n + j}', end= " ")
        j = j + 1
    print()

#dlaczego to mi się nie powtarza?

    
    