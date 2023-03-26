guests_count = int(input())
cover_charge = float(input())
budget = float(input())

cake_cost = budget * 0.1
total_cost = 0

if 10 <= guests_count <=15:
    cover_charge *= 0.85
elif 15 < guests_count <=20:
    cover_charge *= 0.8
elif guests_count > 20:
    cover_charge *= 0.75

total_cost = guests_count * cover_charge + cake_cost

if budget >= total_cost:
    print(f"It is party time! {budget - total_cost:.2f} leva left.")
else:
    print(f"No party! {total_cost - budget:.2f} leva needed.")
