location_count = int(input())

for _ in range(location_count):
    average_yield_per_day = float(input())
    days_count = int(input())
    total_yield = 0

    for _ in range(days_count):
        yield_day = float(input())
        total_yield += yield_day

    average_yield = total_yield / days_count

    if average_yield >= average_yield_per_day:
        print(f"Good job! Average gold per day: {average_yield:.2f}.")
    else:
        print(f"You need {average_yield_per_day - average_yield:.2f} gold.")
