sum_prime_numbers = 0
sum_non_prime_numbers = 0

while True:
    user_input = input()

    if user_input == "stop":
        break
    else:
        user_input = int(user_input)

    if user_input < 0:
        print("Number is negative.")
        continue

    for i in range(2, user_input):
        if user_input % i == 0:
            sum_non_prime_numbers += user_input
            break
    else:
        sum_prime_numbers += user_input




print(f"Sum of all prime numbers is: {sum_prime_numbers}")
print(f"Sum of all non prime numbers is: {sum_non_prime_numbers}")