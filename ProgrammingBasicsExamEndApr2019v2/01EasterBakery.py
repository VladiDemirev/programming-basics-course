flour_cost = float(input())
flour_count = float(input())
sugar_count = float(input())
egg_carton_count = int(input())
yeast_count = int(input())

sugar_cost = flour_cost * 0.75
egg_carton_cost = flour_cost * 1.1
yeast_cost = sugar_cost * 0.2

total_cost = (flour_cost * flour_count) + (sugar_cost * sugar_count) \
    + (egg_carton_cost * egg_carton_count) + (yeast_cost * yeast_count)

print(f"{total_cost:.2f}")