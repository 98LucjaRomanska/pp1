age = int(input("Enter the dog's age in human years: "))
dogage = 0
if age <= 2:
    dogage = age*(10.5)

elif age > 2:
    dogage =int(10.5*2 + (age-2)*4)
    
print(f"The dog's age in dog's years is {dogage} years.")
