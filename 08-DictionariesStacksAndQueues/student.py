student = { 'name':'John', 'age':26, 'courses': ['Math','CompSci']} 
# key: value (value of the key)
#specify a value
print(student['name']) 
print(student.get('name'))
#for jey which does not exist
print(student.get('phone', '_Not Found_'))
#changing value
student['phone']='555-333-222'
student['name']='Jane'

student.update({'name':'John', 'age':26, 'courses': ['Math','CompSci', 'Biology'], 'married': False})
print(student)

del student['age']
print(student)
name = student.pop('name')
#we've dropped the value but also created a new variable
print(student)
print(name) #new variable
student["name"]='Jane'
print(' ')
for key in student:
    print(key)

for key,val in student.items():
    print(key,":", val)

