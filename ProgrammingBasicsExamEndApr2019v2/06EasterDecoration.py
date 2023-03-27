clients_count = int(input())

total_cost = 0

for _ in range(clients_count):

    cost = 0
    products_count = 0

    while True:
        user_input = input()

        if user_input == "Finish":
            if products_count % 2 == 0:
                cost *= 0.80
            total_cost += cost

            print(f"You purchased {products_count} items for {cost:.2f} leva.")
            break

        if user_input == "basket":
            cost += 1.50
        elif user_input == "wreath":
            cost += 3.80
        if user_input == "chocolate bunny":
            cost += 7

        products_count += 1

else:
    print(f"Average bill per client is: {total_cost / clients_count:.2f} leva.")
