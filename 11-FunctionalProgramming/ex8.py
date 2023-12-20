def speed(x):
    y = x / 1000
    res = int(y*3600)
    return f'{x} m/s = {res} km/h' 
def mskm(ms):
    return ms*3.6

if __name__=="__main__":
    print(mskm(10))
    print(speed(10))
    print(speed(35))
