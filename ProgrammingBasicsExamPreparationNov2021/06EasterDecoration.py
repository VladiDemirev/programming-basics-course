COST_BASKET = 1.50
COST_WREATH = 3.80
COST_BUNNY = 7

end_cost = 0
end_cost_all_clients = 0
num_all_products = 0
is_finished = False

num_clients = int(input())

for people in range(1, num_clients + 1):

    num_baskets = 0
    num_wreaths = 0
    num_bunnies = 0

    while True:
        type_purchase = input()

        if type_purchase == "Finish":
            is_finished = True
            break

        if type_purchase == "basket":
            num_baskets += 1
        elif type_purchase == "wreath":
            num_wreaths += 1
        elif type_purchase == "chocolate bunny":
            num_bunnies += 1

        num_all_products = num_baskets + num_wreaths + num_bunnies

        end_cost = (num_baskets * COST_BASKET) + (num_wreaths * COST_WREATH) \
                    + (num_bunnies * COST_BUNNY)

    if is_finished:

        if num_all_products % 2 == 0:
            end_cost = end_cost * 0.8

        end_cost_all_clients += end_cost

        print(f"You purchased {num_all_products} items for {end_cost:.2f} leva.")
        continue

print(f"Average bill per client is: {end_cost_all_clients / num_clients:.2f} leva.")
