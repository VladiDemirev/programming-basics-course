from math import floor, ceil

days_absent = int(input())
food_left = int(input())
food_first_deer = float(input())
food_second_deer = float(input())
food_third_deer = float(input())

food_needed = (food_first_deer * days_absent) + (food_second_deer * days_absent) \
                    + (food_third_deer * days_absent)

if food_left >= food_needed:
    print(f"{floor(food_left - food_needed)} kilos of food left.")
else:
    print(f"{ceil(food_needed - food_left)} more kilos of food are needed.")
