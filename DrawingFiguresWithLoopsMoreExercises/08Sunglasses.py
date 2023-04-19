from math import floor

user_input = int(input())

print(("*" * (2 * user_input)) + (user_input * " ") + ("*" * (2 * user_input)))

for row2 in range(user_input - 2):
    if row2 == floor((user_input - 1) / 2) - 1:
        print("*" + ("/" * (2 * user_input - 2)) + "*" + (user_input * "|")
              + "*" + ("/" * (2 * user_input - 2)) + "*")
    else:
        print("*" + ("/" * (2 * user_input - 2)) + "*" + (user_input * " ")
              + "*" + ("/" * (2 * user_input - 2)) + "*")

print(("*" * (2 * user_input)) + (user_input * " ") + ("*" * (2 * user_input)))