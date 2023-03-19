user_input = int(input())
printed_numbers = 0
current_number = 0

is_number_reached = False

for row in range(1, user_input + 1):
    for col in range(1, row + 1):
        current_number += 1
        print(f"{current_number}", end=" ")

        if row == col:
            print("")
        if current_number == user_input:
            is_number_reached = True
            break

    if is_number_reached:
        break







