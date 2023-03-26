destination = input()
dates = input()
stays_count = int(input())

total_cost = 0

if destination == "France":
    if dates == "21-23":
        cost = 30
    elif dates == "24-27":
        cost = 35
    else:
        cost = 40

elif destination == "Italy":
    if dates == "21-23":
        cost = 28
    elif dates == "24-27":
        cost = 32
    else:
        cost = 39

else:
    if dates == "21-23":
        cost = 32
    elif dates == "24-27":
        cost = 37
    else:
        cost = 43

total_cost = stays_count * cost

print(f"Easter trip to {destination} : {total_cost:.2f} leva.")
