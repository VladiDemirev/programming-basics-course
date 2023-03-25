budget = float(input())
support = int(input())
clothes = float(input())

background = budget * 0.10

if support > 150:
    clothes *= 0.90

cost = background + clothes * support

if cost > budget:
    print("Not enough money!")
    print(f"Wingard needs {cost - budget:.2f} leva more.")
else:
    print("Action!")
    print(f"Wingard starts filming with {budget - cost:.2f} leva left.")







