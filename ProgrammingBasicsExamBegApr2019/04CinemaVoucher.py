voucher = int(input())
tickets = 0
product = 0

while True:
    user_input = input()

    if user_input == "End":
        break
    elif len(user_input) > 8:
        cost = ord(user_input[0]) + ord((user_input[1]))
        if cost > voucher:
            break
        else:
            tickets += 1
    else:
        cost = ord(user_input[0])
        if cost > voucher:
            break
        else:
            product += 1

    voucher -= cost

print(f"{tickets}")
print(f"{product}")

