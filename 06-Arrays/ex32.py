def occurs(number, array):
    for i in array:
        if i == number:
            x = True
            n = f'number {number} appears in the array'
            break
        else:
            x = False
            n = f"number {number} doesn't appear in the array"
            continue
    return f'{number}: {n}'

if __name__=="__main__":
    print(occurs(5,[15,38,7,23,14]))
    print(occurs(23,[15,38,7,23,14]))