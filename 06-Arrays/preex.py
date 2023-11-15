arr=[33,22,44,55,66] #tablica: sekwencja wartości jednego typu
list=[True, False, 3.14, "Romeo"] #lista:różne typy wartości

n=arr[2] 
arr[3]=345

print(arr[3], 50*"-") #przypisanie do czwartej komórki


for n in arr: #wykonana tyle razy ile jest zmiennych w tab
    if n%2==0:
        print(n)

print(80*"-")
i= 0
while i<len(arr):
    print(arr[i])
    i+=1
    