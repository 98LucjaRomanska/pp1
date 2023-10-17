password =input('Enter password: ')
if len(password) >=8:
    password = True
else: 
    password = False

print("Password is valid: ", password)