import random

def generate_number():
    x = random.randint(1,10)
    int(x)
    return int(x)

if __name__ =="__main__":
    print(generate_number())
    print(type(generate_number()))
    