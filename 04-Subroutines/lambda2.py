lambda x: 3*x + 1
g = lambda x: 3*x + 1
print(g(7), g(2))

lambda fn, ln: fn.strip().title() + " " + ln.strip().title()
fl = lambda fn, ln: fn.strip().title() + " " + ln.strip().title()
print( fl( "leonard", "euler"))

lambda kg, cm: kg/(cm*0.01)**2
function = lambda kg, cm: kg/(cm*0.01)**2
mass_index = function(81,182)
x = 10
print(f"Peter's BMI is: {mass_index:.2f}")