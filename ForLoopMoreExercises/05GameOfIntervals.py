num_moves = int(input())

number0_9 = 0
number10_19 = 0
number20_29 = 0
number30_39 = 0
number40_50 = 0
num_invalid_numbers = 0
result = 0

for i in range(0, num_moves):
    number = int(input())
    if 0 <= number <= 9:
        number0_9 += 1
        result += number * 0.2
    elif 10 <= number <= 19:
        number10_19 += 1
        result += number * 0.3
    elif 20 <= number <= 29:
        number20_29 += 1
        result += number * 0.4
    elif 30 <= number <= 39:
        number30_39 += 1
        result += 50
    elif 40 <= number <= 50:
        number40_50 += 1
        result += 100
    else:
        num_invalid_numbers += 1
        result /= 2

print(f"{result:.2f}")
print(f"From 0 to 9: {number0_9 / num_moves * 100:.2f}%")
print(f"From 10 to 19: {number10_19 / num_moves * 100:.2f}%")
print(f"From 20 to 29: {number20_29 / num_moves * 100:.2f}%")
print(f"From 30 to 39: {number30_39 / num_moves * 100:.2f}%")
print(f"From 40 to 50: {number40_50 / num_moves * 100:.2f}%")
print(f"Invalid numbers: {num_invalid_numbers / num_moves * 100:.2f}%")
