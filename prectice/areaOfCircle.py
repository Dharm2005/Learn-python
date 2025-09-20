# this program calculate area of circle
# formula  area = πr²

import math

pi = math.pi
radius = float(input("Enter radius of circle: "))

result = pi * math.pow(radius,2)

print(f"Circumference of circle is {result}")