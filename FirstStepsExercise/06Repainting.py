PRICE_NYLON = 1.50
PRICE_PAINT = 14.50
PRICE_THINNER = 5.00
PRICE_BAGS = 0.40

nylon = int(input())
nylon = nylon + 2

paint = int(input())
paint = paint + paint * 0.1

thinner = int(input())

material_cost = (PRICE_NYLON * nylon) + (PRICE_PAINT * paint) \
                + (PRICE_THINNER * thinner) + PRICE_BAGS

hours = int(input())

price_painters = material_cost * 0.3

total_cost = material_cost + (price_painters * hours)

print(total_cost)