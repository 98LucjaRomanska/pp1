#n = input('numbers for array: ')
n = "8,2,5,1,9"
array = n.split(",")
arr2nd =n.split(",")
print(array)
power2nd = []
for i in range(len(array)):
    array[i] = int(array[i])**2
    power2nd.append(array[i])
print(power2nd)

power2nd.clear()
print(" ")
print(arr2nd)
power2nd =[int(arr2nd[i])**2 for i in range(len(arr2nd))]
print(power2nd)
f = "f"
print(f)
f = 17
print(f)

