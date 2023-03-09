import math
from math import floor, ceil

# User input
vineyard_area_X = int(input())
grape_sq_m_Y = float(input())
needed_ltr_wine_Z = int(input())
num_workers = int(input())

# Calculations
grape_for_wine_area = vineyard_area_X * 0.4
vineyard_yield = grape_for_wine_area * grape_sq_m_Y
produced_liters_wine = vineyard_yield / 2.5

# Conditions
if produced_liters_wine < needed_ltr_wine_Z:
    print(f"It will be a tough winter! More "
          f"{math.floor(needed_ltr_wine_Z - produced_liters_wine)} "
          f"liters wine needed.")
else:
    print(f"Good harvest this year! Total wine: "
          f"{math.floor(produced_liters_wine)} liters.")
    print(f"{math.ceil(produced_liters_wine - needed_ltr_wine_Z)} "
f"liters left -> "
          f"{math.ceil((produced_liters_wine - needed_ltr_wine_Z) / num_workers)} "
          f"liters per person.")