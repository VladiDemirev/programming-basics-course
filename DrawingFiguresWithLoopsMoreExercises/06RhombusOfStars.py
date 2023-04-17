user_input = int(input())

for row in range(1, user_input + 1):
    if user_input == 1:
        print("*")
    else:
        print(" " * (user_input - row) + "*" + (row - 1) * " *")

for row in range(user_input - 1, 0, -1):
    print(" " * (user_input - row) + "*" + (row - 1) * " *")


