import math
from math import floor, ceil

MAGNOLIA = 3.25
ZIUMBUL = 4
ROSE = 3.50
CACTUS = 8

num_magnolia = int(input())
num_ziumbul = int(input())
num_rose = int(input())
num_cactus = int(input())
gift_price = float(input())

earnings_before_tax = (MAGNOLIA * num_magnolia) + (ZIUMBUL * num_ziumbul) \
              + (ROSE * num_rose) + (CACTUS * num_cactus)
tax_cost = earnings_before_tax * 0.05
earnings_net = earnings_before_tax - tax_cost

if earnings_net >= gift_price:
    print(f"She is left with {math.floor(earnings_net - gift_price)} leva.")
else:
    print(f"She will have to borrow {math.ceil(gift_price - earnings_net)} leva.")



