from math import ceil

average_speed = float(input())
fuel = float(input())

time = 384400 * 2 / average_speed
total_time = time + 3
total_fuel = 384400 * 2 * fuel / 100

print(f"{ceil(total_time)}")
print(f"{total_fuel:.0f}")
