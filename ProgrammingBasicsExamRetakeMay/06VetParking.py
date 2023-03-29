days = int(input())
hours = int(input())

total_cost = 0

for i in range(1, days + 1):
    day_cost = 0

    for j in range(1, hours + 1):
        if i % 2 == 0 and j % 2 != 0:
            cost = 2.50
        elif i % 2 != 0 and j % 2 == 0:
            cost = 1.25
        else:
            cost = 1

        day_cost += cost

    total_cost += day_cost
    print(f"Day: {i} - {day_cost:.2f} leva")

print(f"Total: {total_cost:.2f} leva")

