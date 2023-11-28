import random
arr0 = [3,45,6,76,89,2]
arr1 = [3.14,6.56,116,-89,-2]

def rand_elem(array):
    return random.choice(array)

if __name__=="__main__":
    print(rand_elem(arr0))
    print(rand_elem(arr1))