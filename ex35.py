for i in range(1,31):
    if i%3 == 0 and i%5 != 0:
        print("THREE")
        continue
    elif i%3 != 0 and i%5 == 0:
        print("FIVE")
        continue
    elif i%3 == 0 and i%5 == 0:
        print('BINGO')
        continue
    print(i)



