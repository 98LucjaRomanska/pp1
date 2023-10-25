def hours():
    for i in range(1,25):
         if i <= 12:
            print(i)
         else:
            pm = i - 12
            print(pm)


time24h = input("Enter time (24-hour format): ")
print(int(time24h[:2]))
hh = int(time24h[:2])
print(int(time24h[-2:]))
mm = int(time24h[-2:])

if hh <= 12:
    print(f"{hh}:{mm}am")
elif hh > 12:
    pm = hh - 12
    print(f"{pm}:{mm}pm")
