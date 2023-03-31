num_days = int(input())
hours_per_day = int(input())
total_cost = 0

for day in range(1, num_days + 1):
    cost = 0
    for hour in range(1, hours_per_day + 1):
        if (
                (day % 2 == 0) and
                (hour % 2 != 0)
        ):
            cost += 2.50
        elif (
                (day % 2 != 0) and
                (hour % 2 == 0)
        ):
            cost += 1.25
        else:
            cost += 1

    total_cost += cost

    print(f"Day: {day} - {cost:.2f} leva")

print(f"Total: {total_cost:.2f} leva")