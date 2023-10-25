x = "Decide whether the person has an account on specified platform by printing 0 or 1"
print(x)
twitter = int(input("twitter: "))
facebook = int(input('facebook: '))
instagram = int(input('instagram: '))
print(facebook)
print(twitter)
print(instagram)

print('//')

print("Facebook:", bool(facebook))
print("Twitter:", bool(twitter))
print("Instagram:", bool(twitter))

sum = twitter + facebook + instagram
if twitter + facebook + instagram ==2 or sum == 3:
    print('This person can be a good influencer!')
elif sum < 2: 
    print('This person will not be a good influencer')
elif sum > 3:
    print("You've inserted wrong numbers!")

