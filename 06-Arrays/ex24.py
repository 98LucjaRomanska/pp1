array = [15,8,31,47,2,19]
print(array)
sum= 0
for i in range(len(array)):
    sum += array[i]
a_mean = sum/len(array)
format_a_mean = "{:.2f}".format(a_mean) 
print(format_a_mean)