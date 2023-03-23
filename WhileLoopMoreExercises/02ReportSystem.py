sales_amount = int(input())
payments_count = 0
payments_cash = 0
payments_card = 0
current_cash = 0
current_card = 0

while True:
    product_price = input()

    if product_price == "End":
        print("Failed to collect required money for charity.")
        break

    else:
        product_price = int(product_price)

        payments_count += 1

    if payments_count % 2 != 0:
        if product_price > 100:
            print("Error in transaction!")
        else:
            print("Product sold!")
            payments_cash += 1
            current_cash += product_price

    if payments_count % 2 == 0:
        if product_price < 10:
            print("Error in transaction!")
        else:
            print("Product sold!")
            payments_card += 1
            current_card += product_price

    if (current_cash + current_card) >= sales_amount:
        print(f"Average CS: {current_cash / payments_cash:.2f}")
        print(f"Average CC: {current_card / payments_card:.2f}")
        break


