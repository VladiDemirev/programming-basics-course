# User input
num_km_n = int(input())
day_or_night = input()

# Constants
START_TAX_TAXI = 0.70
DAY_TARIFF_TAXI = 0.79
NIGHT_TARIFF_TAXI = 0.90
TARIFF_BUS = 0.09       # min distance 20km
TARIFF_TRAIN = 0.06       # min distance 100km

# Conditions
if day_or_night == "day" and num_km_n < 20:
    taxi_cost = START_TAX_TAXI + DAY_TARIFF_TAXI * num_km_n
    print(f"{taxi_cost:.2f}")
if day_or_night == "night" and num_km_n < 20:
    taxi_cost = START_TAX_TAXI + NIGHT_TARIFF_TAXI * num_km_n
    print(f"{taxi_cost:.2f}")
if 20 <= num_km_n < 100:
    bus_cost = TARIFF_BUS * num_km_n
    print(f"{bus_cost:.2f}")
if num_km_n >= 100:
    train_cost = TARIFF_TRAIN * num_km_n
    print(f"{train_cost:.2f}")