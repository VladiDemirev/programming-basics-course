fruit = input()
size = input()
gels_count = int(input())

cost = 0

if fruit == "Watermelon":
    if size == "small":
        cost = 2 * 56 * gels_count
    else:
        cost = 5 * 28.70 * gels_count

elif fruit == "Mango":
    if size == "small":
        cost = 2 * 36.66 * gels_count
    else:
        cost = 5 * 19.60 * gels_count

elif fruit == "Pineapple":
    if size == "small":
        cost = 2 * 42.10 * gels_count
    else:
        cost = 5 * 24.80 * gels_count

else:
    if size == "small":
        cost = 2 * 20 * gels_count
    else:
        cost = 5 * 15.20 * gels_count

if 400 <= cost <= 1000:
    cost *= 0.85
elif cost > 1000:
    cost *= 0.50

print(f"{cost:.2f} lv.")