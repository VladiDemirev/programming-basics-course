product = input()
city = input()
quantity = float(input())
total_cost = 0

if city == "Sofia":
    if product == "coffee":
        total_cost = 0.50 * quantity
    elif product == "water":
        total_cost = 0.80 * quantity
    elif product == "beer":
        total_cost = 1.20 * quantity
    elif product == "sweets":
        total_cost = 1.45 * quantity
    elif product == "peanuts":
        total_cost = 1.60 * quantity

elif city == "Plovdiv":
    if product == "coffee":
        total_cost = 0.40 * quantity
    elif product == "water":
        total_cost = 0.70 * quantity
    elif product == "beer":
        total_cost = 1.15 * quantity
    elif product == "sweets":
        total_cost = 1.30 * quantity
    elif product == "peanuts":
        total_cost = 1.50 * quantity

elif city == "Varna":
    if product == "coffee":
        total_cost = 0.45 * quantity
    elif product == "water":
        total_cost = 0.70 * quantity
    elif product == "beer":
        total_cost = 1.10 * quantity
    elif product == "sweets":
        total_cost = 1.35 * quantity
    elif product == "peanuts":
        total_cost = 1.55 * quantity

print(total_cost)