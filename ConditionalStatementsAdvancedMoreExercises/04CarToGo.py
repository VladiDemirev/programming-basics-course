budget = float(input())
season = input()            # Summer or Winter

cost_car = 0
class_car = ""
type_car = ""

if budget <= 100:
    class_car = "Economy class"
    if season == "Summer":
        type_car = "Cabrio"
        cost_car = budget * 0.35
    elif season == "Winter":
        type_car = "Jeep"
        cost_car = budget * 0.65
elif 100 < budget <= 500:
    class_car = "Compact class"
    if season == "Summer":
        type_car = "Cabrio"
        cost_car = budget * 0.45
    elif season == "Winter":
        type_car = "Jeep"
        cost_car = budget * 0.80
elif budget > 500:
    class_car = "Luxury class"
    type_car = "Jeep"
    cost_car = budget * 0.90

print(f"{class_car}")
print(f"{type_car} - {cost_car:.2f}")

