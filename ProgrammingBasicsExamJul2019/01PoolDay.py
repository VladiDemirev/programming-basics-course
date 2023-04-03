from math import ceil

num_people = int(input())
entry_fee = float(input())
price_bed = float(input())
price_umbrella = float(input())

num_beds = ceil(num_people * 0.75)
num_umbrellas = ceil(num_people / 2)

total_cost = entry_fee * num_people + num_beds * price_bed + num_umbrellas * price_umbrella

print(f"{total_cost:.2f} lv.")
