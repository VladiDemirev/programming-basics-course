eggs_size = input()
eggs_color = input()
lot_count = int(input())

lot_cost = 0

if eggs_size == "Large":
    if eggs_color == "Red":
        lot_cost = 16
    elif eggs_color == "Green":
        lot_cost = 12
    else:
        lot_cost = 9

elif eggs_size == "Medium":
    if eggs_color == "Red":
        lot_cost = 13
    elif eggs_color == "Green":
        lot_cost = 9
    else:
        lot_cost = 7

elif eggs_size == "Small":
    if eggs_color == "Red":
        lot_cost = 9
    elif eggs_color == "Green":
        lot_cost = 8
    else:
        lot_cost = 5

total_cost = lot_cost * lot_count
production_cost = total_cost * 0.35
income = total_cost - production_cost

print(f"{income:.2f} leva.")