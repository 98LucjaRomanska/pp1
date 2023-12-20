speed_camera = [48,47,54,50,42,68,39,46]
rult = list(filter(lambda n: n>50, speed_camera))
print(rult)
sum="Speed to high: "
for x in rult:
    sum += str(x) +", "
sum.strip()
print(sum)