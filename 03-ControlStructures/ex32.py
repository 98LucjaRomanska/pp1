quest1 = input('Are you interested in computer science? (Y/N): ')
quest2 = input('Do you like playing computer games? (Y/N): ')
quest3 = input('Do you have an Instagram account? (Y/N): ')

if quest1 =="Y" or quest1 == "y":
    quest1 = 1
elif quest1 =="N" or quest1 =="n":
    quest1 = 0

if bool(quest1)== 1:
    quest1 = "Yes"
elif bool(quest1)==0:
    quest1 ="No"
    
print(f'Interested in computer science: {quest1}')

if quest2 == "Y" or quest2 =="y":
    quest2 = 1
elif quest2 =="N" or quest2=="n":
    quest2 = 0

if bool(quest2) == 1:
    quest2 = "Yes"
elif bool(quest2) == 0:
    quest2 = "No"
print(f'Playing computer games: {quest2}')

if quest3 == "Y" or quest3 =="y":
    quest3 = 1
elif quest3 =="N" or quest3=="n":
    quest3 = 0

if bool(quest3) == 1:
    quest3 = "Yes"
elif bool(quest3) == 0:
    quest3 = "No"
print(f'Has an Instagram account: {quest3}')
