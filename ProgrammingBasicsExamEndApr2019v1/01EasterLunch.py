cake_count = int(input())
egg_cartons_count = int(input())
cookies_count = int(input())

lunch_cost = (cake_count * 3.20) + (egg_cartons_count * 4.35) \
             + (egg_cartons_count * 12 * 0.15) + cookies_count * 5.4

print(f"{lunch_cost:.2f}")