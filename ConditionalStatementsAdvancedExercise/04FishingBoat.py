budget = int(input())
season = input()
num_fishermen = int(input())

money_needed = 0

# OPTION 1

if season == "Spring":
    money_needed = 3000
elif season == "Summer" or season == "Autumn":
    money_needed = 4200
elif season == "Winter":
    money_needed = 2600

if num_fishermen <= 6:
    money_needed *= 0.9
elif 7 <= num_fishermen <= 11:
    money_needed *= 0.85
elif num_fishermen >= 12:
    money_needed *= 0.75

if num_fishermen % 2 == 0 and season != "Autumn":
    money_needed *= 0.95

if budget >= money_needed:
    print(f"Yes! You have {abs(budget - money_needed):.2f} leva left.")
else:
    print(f"Not enough money! You need {abs(budget - money_needed):.2f} leva.")

# OPTION 2

# if season == "Spring":
#     RENT_SPRING = 3000
#     if num_fishermen <= 6:
#         money_needed = RENT_SPRING * 0.9
#     elif 7 <= num_fishermen <= 11:
#         money_needed = RENT_SPRING * 0.85
#     elif num_fishermen >= 12:
#         money_needed = RENT_SPRING * 0.75
#
# elif season == "Summer" or season == "Autumn":
#     RENT_SUMMER_AUTUMN = 4200
#     if num_fishermen <= 6:
#         money_needed = RENT_SUMMER_AUTUMN * 0.9
#     elif 7 <= num_fishermen <= 11:
#         money_needed = RENT_SUMMER_AUTUMN * 0.85
#     elif num_fishermen >= 12:
#         money_needed = RENT_SUMMER_AUTUMN * 0.75
#
# elif season == "Winter":
#     RENT_WINTER = 2600
#     if num_fishermen <= 6:
#         money_needed = RENT_WINTER * 0.9
#     elif 7 <= num_fishermen <= 11:
#         money_needed = RENT_WINTER * 0.85
#     elif num_fishermen >= 12:
#         money_needed = RENT_WINTER * 0.75
#
# if num_fishermen % 2 == 0 and season != "Autumn":
#     money_needed *= 0.95
#
# if budget >= money_needed:
#     print(f"Yes! You have {abs(budget - money_needed):.2f} leva left.")
# else:
#     print(f"Not enough money! You need {abs(budget - money_needed):.2f} leva.")
