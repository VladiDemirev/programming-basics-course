budget = float(input())
fuel = float(input())
day = input()

total_fuel = fuel * 2.10
cost = total_fuel + 100

if day == "Saturday":
    cost *= 0.9
else:
    cost *= 0.8

if budget >= cost:
    print(f"Safari time! Money left: {budget - cost:.2f} lv.")
else:
    print(f"Not enough money! Money needed: {cost - budget:.2f} lv.")

