car_speed = float(input('Enter car speed:'))
speed_limit_min = 40
speed_limit_max = 140
if car_speed< speed_limit_min:
    print('Warning: invalid car speed! ')
elif car_speed >= speed_limit_min and car_speed <= speed_limit_max:
    print('Permissible speed')
elif car_speed > speed_limit_max:
    print('Warning: speed has been exceeded to impermissible level!')