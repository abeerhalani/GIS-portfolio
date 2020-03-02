#This calculates the area of a circle when the user inputs a value for the radius

from math import pi
r = float(raw_input("Input the radius of the circle: "))
print ("The area of the circle with radius " + str(r) + " is: " + str(pi * r**2))