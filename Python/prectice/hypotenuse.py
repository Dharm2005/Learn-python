# this program is to calculate hypotenuse of right triangle

import math

sideA = float(input("Enter side A of triangle: "))
sideB = float(input("Enter side B of triangle: "))

result = math.sqrt(pow(sideA,2) + pow(sideB,2))

print(f"result is {result}")