import math
from math import pi

radius = float(input())

circle_area = pi * (radius ** 2)
circle_perimeter = 2 * pi * radius

print(f"{circle_area:.2f}")
print(f"{circle_perimeter:.2f}")