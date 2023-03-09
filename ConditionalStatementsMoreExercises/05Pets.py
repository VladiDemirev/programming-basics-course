import math
from math import floor, ceil

num_days = int(input())
food_left = int(input())
dog_food_day = float(input())
cat_food_day = float(input())
turtle_food_day = float(input()) / 1000

total_food_eaten = (dog_food_day + cat_food_day + turtle_food_day) * num_days

if food_left >= total_food_eaten:
    print(f"{math.floor(food_left - total_food_eaten)} kilos of food left.")
else:
    print(f"{math.ceil(total_food_eaten - food_left)} more kilos of food are needed.")