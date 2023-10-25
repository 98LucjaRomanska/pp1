x = int(input("Enter x:"))
y = int(input("Enter y:"))
quadrant = 0 
if x > 0 and y > 0: 
    quadrant = 1
    print(f"Point P({x},{y}) is in the first quadrant of the coordinate system.")
elif  x < 0 and y > 0: 
    quadrant = 2
    print(f"Point P({x},{y}) is in the second quadrant of the coordinate system.")
elif x < 0 and y < 0: 
    quadrant = 3
    print(f"Point P({x},{y}) is in the third quadrant of the coordinate system.")
elif x > 0 and y < 0:
    quadrant = 4 
    print(f"Point P({x},{y}) is in the fourth quadrant of the coordinate system. ")
elif x == 0 and y == 0:
    quadrant = 0
    print(f"Point P({x},{y}) is the beginning of a coordinate system.")