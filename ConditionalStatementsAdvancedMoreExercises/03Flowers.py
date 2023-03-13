num_hrizantemas = int(input())
num_roses = int(input())
num_tulips = int(input())
season = input()                # Spring, Summer, Autumn, Winter
is_holiday = input()            # Y / N

COST_HRIZANTEMAS = 0
COST_ROSES = 0
COST_TULIPS = 0
bouquet_cost = 0

ARRANGING_COST = 2

if season == "Spring" or season == "Summer":
    COST_HRIZANTEMAS = 2
    COST_ROSES = 4.10
    COST_TULIPS = 2.50
elif season == "Autumn" or season == "Winter":
    COST_HRIZANTEMAS = 3.75
    COST_ROSES = 4.50
    COST_TULIPS = 4.15

if is_holiday == "Y":
    bouquet_cost = (num_hrizantemas * COST_HRIZANTEMAS * 1.15) \
               + (num_roses * COST_ROSES * 1.15) \
               + (num_tulips * COST_TULIPS * 1.15)
elif is_holiday == "N":
    bouquet_cost = (num_hrizantemas * COST_HRIZANTEMAS) \
               + (num_roses * COST_ROSES) \
               + (num_tulips * COST_TULIPS)

if season == "Spring" and num_tulips > 7:
    bouquet_cost = bouquet_cost - bouquet_cost * 0.05
if season == "Winter" and num_roses >= 10:
    bouquet_cost = bouquet_cost - bouquet_cost * 0.1
if (num_hrizantemas + num_roses + num_tulips) > 20:
    bouquet_cost = bouquet_cost - bouquet_cost * 0.2

final_bouquet_cost = bouquet_cost + ARRANGING_COST

print(f"{final_bouquet_cost:.2f}")
