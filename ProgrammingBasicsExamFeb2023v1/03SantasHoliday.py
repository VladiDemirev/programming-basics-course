days_stay = int(input())
room_type = input()
grade = input()

total_cost = 0

if room_type == "room for one person":
    cost = 18
elif room_type == "apartment":
    cost = 25
    if days_stay < 10:
        cost *= 0.7
    elif 10 <= days_stay <= 15:
        cost *= 0.65
    else:
        cost *= 0.5
else:
    cost = 35
    if days_stay < 10:
        cost *= 0.9
    elif 10 <= days_stay <= 15:
        cost *= 0.85
    else:
        cost *= 0.8

total_cost = (days_stay - 1) * cost

if grade == "positive":
    total_cost *= 1.25
else:
    total_cost *= 0.9

print(f"{total_cost:.2f}")
