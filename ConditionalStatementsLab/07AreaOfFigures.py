import math
from math import pi

figure = input()

area = 0

# choose between square, rectangle, circle or triangle
if figure == "square":
    a = float(input())
    area = a ** 2

elif figure == "rectangle":
    a = float(input())
    b = float(input())
    area = a * b

elif figure == "circle":
    r = float(input())
    area = pi * (r ** 2)

elif figure == "triangle":
    length = float(input())
    height = float(input())
    area = (length * height) / 2

print("{:.3f}".format(area))