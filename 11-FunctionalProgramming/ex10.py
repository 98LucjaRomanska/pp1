distance = 10
hours = 2
minutes = 55
def avg_speed(distance,hours, minutes):
    return f'Average speed: {round(distance/hours + minutes/60), 1}'

print(avg_speed(distance,hours,minutes))