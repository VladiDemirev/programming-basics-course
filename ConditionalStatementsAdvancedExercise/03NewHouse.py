type_flower = input()
num_flowers = int(input())
budget = int(input())

COST_ROSES = 5
COST_DAHLIA = 3.80
COST_TULIPS = 2.80
COST_NARCISSUS = 3
COST_GLADIOLUS = 2.50

total_cost = 0

if type_flower == "Roses":
    total_cost = num_flowers * 5
    if num_flowers > 80:
        total_cost *= 0.9

elif type_flower == "Dahlias":
    total_cost = num_flowers * 3.80
    if num_flowers > 90:
        total_cost *= 0.85

elif type_flower == "Tulips":
    total_cost = num_flowers * 2.80
    if num_flowers > 80:
        total_cost *= 0.85

elif type_flower == "Narcissus":
    total_cost = num_flowers * 3
    if num_flowers < 120:
        total_cost *= 1.15

elif type_flower == "Gladiolus":
    total_cost = num_flowers * 2.50
    if num_flowers < 80:
        total_cost *= 1.2

if budget >= total_cost:
    print(f"Hey, you have a great garden with {num_flowers} {type_flower} "
          f"and {abs(budget - total_cost):.2f} leva left.")
else:
    print(f"Not enough money, you need {abs(budget - total_cost):.2f} "
          f"leva more.")