cent = int(input('Enter your height in cm: '))
m = 0.01*cent
kg = int(input('Enter your weight in kg: '))
bmi = int(kg/(m**2))
print('Your BMI index: ', bmi )
if bmi <= 25.0 and bmi >= 18.5:
    bmi = True
else:
    bmi = False
print('Correct weight: ',bmi)

