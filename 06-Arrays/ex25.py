array = [15,8,31,47,2,19]
print(array)
i = 0
sum = 0
while i<len(array):
    sum += array[i]
    i+=1
a_mean = sum/len(array)
format_a_mean = '{:.2f}'.format(a_mean)
print(format_a_mean)