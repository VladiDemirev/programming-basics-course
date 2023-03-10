days_stay = int(input()) - 1
room_type = input()
assesment = input()

cost_stay = 0

if room_type == "room for one person":
    cost_stay = days_stay * 18

elif room_type == "apartment":
    if days_stay < 10:
        cost_stay = (days_stay * 25) * 0.7
    elif 10 <= days_stay <= 15:
        cost_stay = (days_stay * 25) * 0.65
    else:
        cost_stay = (days_stay * 25) * 0.5

elif room_type == "president apartment":
    if days_stay < 10:
        cost_stay = (days_stay * 35) * 0.9
    elif 10 <= days_stay <= 15:
        cost_stay = (days_stay * 35) * 0.85
    else:
        cost_stay = (days_stay * 35) * 0.8

if assesment == "positive":
    cost_stay *= 1.25
elif assesment == "negative":
    cost_stay *= 0.9

print(f"{cost_stay:.2f}")