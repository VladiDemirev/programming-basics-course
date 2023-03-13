season = input()            # Spring, Summer, Autumn, Winter
km_per_month = float(input())

NUM_MONTHS = 4
revenue = 0

if season == "Spring" or season == "Autumn":
    if km_per_month <= 5000:
        revenue = 0.75         # lv./km
    if 5000 < km_per_month <= 10000:
        revenue = 0.95
elif season == "Summer":
    if km_per_month <= 5000:
        revenue = 0.90         # lv./km
    if 5000 < km_per_month <= 10000:
        revenue = 1.10
elif season == "Winter":
    if km_per_month <= 5000:
        revenue = 1.05         # lv./km
    if 5000 < km_per_month <= 10000:
        revenue = 1.25

if 10000 < km_per_month <= 20000:
        revenue = 1.45

gross_revenue = km_per_month * revenue * NUM_MONTHS
tax = gross_revenue * 0.1
net_revenue = gross_revenue - tax

print(f"{net_revenue:.2f}")