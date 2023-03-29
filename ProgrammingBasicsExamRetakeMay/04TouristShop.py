budget = float(input())
total_cost = 0
products = 0

while True:
    user_input = input()

    if user_input == "Stop":
        print(f"You bought {products} products for {total_cost:.2f} leva.")
        break

    products += 1
    price = float(input())

    if products % 3 == 0:
        price *= 0.5

    total_cost += price

    if total_cost > budget:
        print("You don't have enough money!")
        print(f"You need {total_cost - budget:.2f} leva!")
        break

