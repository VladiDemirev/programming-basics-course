budget = float(input())
season = input()            # Summer or Winter

location = ""
accommodation = ""
cost_stay = 0

if budget <= 1000:
    accommodation = "Camp"
    if season == "Summer":
        location = "Alaska"
        cost_stay = budget * 0.65
    if season == "Winter":
        location = "Morocco"
        cost_stay = budget * 0.45
elif 1000 < budget <= 3000:
    accommodation = "Hut"
    if season == "Summer":
        location = "Alaska"
        cost_stay = budget * 0.80
    if season == "Winter":
        location = "Morocco"
        cost_stay = budget * 0.60
elif budget > 3000:
    accommodation = "Hotel"
    if season == "Summer":
        location = "Alaska"
        cost_stay = budget * 0.90
    if season == "Winter":
        location = "Morocco"
        cost_stay = budget * 0.90

print(f"{location} - {accommodation} - {cost_stay:.2f} ")