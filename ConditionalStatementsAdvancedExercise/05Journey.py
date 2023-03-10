# OPTION 1

# budget = float(input())
# season = input()
#
# destination = ""
# accommodation = ""
# money_spent = 0

# if budget <= 100:
#     destination = "Bulgaria"
#     if season == "summer":
#         accommodation = "Camp"
#         money_spent = budget * 0.3
#     else:
#         accommodation = "Hotel"
#         money_spent = budget * 0.7
#
# elif budget <= 1000:
#     destination = "Balkans"
#     if season == "summer":
#         accommodation = "Camp"
#         money_spent = budget * 0.4
#     else:
#         accommodation = "Hotel"
#         money_spent = budget * 0.8
#
# else:
#     destination = "Europe"
#     accommodation = "Hotel"
#     money_spent = budget * 0.9
#
# print(f"Somewhere in {destination}")
# print(f"{accommodation} - {money_spent:.2f}")

# OPTION 2

budget = float(input())
season = input()

destination = ""
accommodation = ""
money_spent = 0

if budget <= 100:
    destination = "Bulgaria"
    if season == "summer":
        money_spent = budget * 0.3
    elif season == "winter":
        money_spent = budget * 0.7

elif 100 < budget <= 1000:
    destination = "Balkans"
    if season == "summer":
        money_spent = budget * 0.4
    elif season == "winter":
        money_spent = budget * 0.8

elif budget > 1000:
    destination = "Europe"
    money_spent = budget * 0.9

if season == "summer" and destination != "Europe":
    accommodation = "Camp"
elif season == "winter":
    accommodation = "Hotel"
else:
    accommodation = "Hotel"

print(f"Somewhere in {destination}")
print(f"{accommodation} - {money_spent:.2f}")
