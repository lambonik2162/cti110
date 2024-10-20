# Komna Lamboni
# 10/05/2024
# P2LAB1
# Writing code that performs mathematical calculations and displays information to users.

import math

# Get radius from the user
radius=float(input())

# Compute the diameter, the circumference, and the area
diameter=2*radius
circumference=2*math.pi*radius
area=math.pi*(radius**2)

# Format the results
formatted_diameter = "{:.1f}".format(diameter)
formatted_circumference = "{:.2f}".format(circumference)
formatted_area = "{:.3f}".format(area)

# Display the results
print('What is the radius of the circle?',radius)
print('The diameter of the circle is',formatted_diameter )
print('The circumference of the circle is',formatted_circumference)
print('The area of the circle is',formatted_area)
