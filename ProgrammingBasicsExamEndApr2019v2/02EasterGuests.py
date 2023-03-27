from math import ceil

guests_count = int(input())
budget = int(input())

total_cakes = ceil(guests_count / 3) * 4
total_eggs = guests_count * 2 * 0.45

total_cost = total_eggs + total_cakes

if budget >= total_cost:
    print(f"Lyubo bought {ceil(guests_count / 3)} Easter bread and {guests_count * 2} eggs.")
    print(f"He has {budget - total_cost:.2f} lv. left.")
else:
    print("Lyubo doesn't have enough money.")
    print(f"He needs {total_cost - budget:.2f} lv. more.")
