user_input = int(input())

for i in range(user_input + 1):
    print(" " * (user_input - i) + "*" * i + " | " + "*" * i)
