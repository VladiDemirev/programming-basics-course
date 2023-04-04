destination = input()
reservation_dates = input()
num_stay = int(input())

cost_stay = 0

if destination == "France":
    if reservation_dates == "21-23":
        cost_stay = 30
    elif reservation_dates == "24-27":
        cost_stay = 35
    else:
        cost_stay = 40

if destination == "Italy":
    if reservation_dates == "21-23":
        cost_stay = 28
    elif reservation_dates == "24-27":
        cost_stay = 32
    else:
        cost_stay = 39

if destination == "Germany":
    if reservation_dates == "21-23":
        cost_stay = 32
    elif reservation_dates == "24-27":
        cost_stay = 37
    else:
        cost_stay = 43

total_expenses = cost_stay * num_stay

print(f"Easter trip to {destination} : {total_expenses:.2f} leva.")