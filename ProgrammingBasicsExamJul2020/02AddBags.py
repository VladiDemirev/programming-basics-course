luggage_cost_over_20kg = float(input())
luggage_weight = float(input())
days_to_trip = int(input())
luggage_count = int(input())

luggage_cost = 0

if luggage_weight < 10:
    luggage_cost = luggage_cost_over_20kg * 0.2
elif 10 <= luggage_weight <= 20:
    luggage_cost = luggage_cost_over_20kg * 0.5
else:
    luggage_cost = luggage_cost_over_20kg

if days_to_trip > 30:
    luggage_cost *= 1.1
elif 7 <= days_to_trip <= 30:
    luggage_cost *= 1.15
else:
    luggage_cost *= 1.4

total_luggage_cost = luggage_cost * luggage_count

print(f"The total price of bags is: {total_luggage_cost:.2f} lv. ")