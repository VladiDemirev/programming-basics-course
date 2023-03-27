start_eggs_count = int(input())
eggs_sold = 0

while True:
    user_input = input()

    if user_input == "Close":
        print("Store is closed!")
        print(f"{eggs_sold} eggs sold.")
        break

    new_eggs = int(input())

    if user_input == "Buy" and new_eggs > start_eggs_count:
        print("Not enough eggs in store!")
        print(f"You can buy only {start_eggs_count}.")
        break

    if user_input == "Buy":
        eggs_sold += new_eggs
        start_eggs_count -= new_eggs
    else:
        start_eggs_count += new_eggs


