money = float(input())
gender = input()
age = int(input())
sport = input()

cost = 0

if gender == "m":
    if sport == "Gym":
        cost = 42
    elif sport == "Boxing":
        cost = 41
    elif sport == "Yoga":
        cost = 45
    elif sport == "Zumba":
        cost = 34
    elif sport == "Dances":
        cost = 51
    elif sport == "Pilates":
        cost = 39

if gender == "f":
    if sport == "Gym":
        cost = 35
    elif sport == "Boxing":
        cost = 37
    elif sport == "Yoga":
        cost = 42
    elif sport == "Zumba":
        cost = 31
    elif sport == "Dances":
        cost = 53
    elif sport == "Pilates":
        cost = 37

if age <= 19:
    cost *= 0.8

if money >= cost:
    print(f"You purchased a 1 month pass for {sport}.")
else:
    print(f"You don't have enough money! You need ${cost - money:.2f} more.")



