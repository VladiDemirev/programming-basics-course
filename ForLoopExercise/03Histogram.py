count_number = int(input())

sum_numbers1 = 0
sum_numbers2 = 0
sum_numbers3 = 0
sum_numbers4 = 0
sum_numbers5 = 0

p1 = 0
p2 = 0
p3 = 0
p4 = 0
p5 = 0

for i in range(1, count_number+1):
    user_input = int(input())
    if user_input < 200:
        sum_numbers1 += 1
        p1 = sum_numbers1 / count_number * 100
    elif 200 <= user_input <= 399:
        sum_numbers2 += 1
        p2 = sum_numbers2 / count_number * 100
    elif 400 <= user_input <= 599:
        sum_numbers3 += 1
        p3 = sum_numbers3 / count_number * 100
    elif 600 <= user_input <= 799:
        sum_numbers4 += 1
        p4 = sum_numbers4 / count_number * 100
    elif user_input >= 800:
        sum_numbers5 += 1
        p5 = sum_numbers5 / count_number * 100

print(f"{p1:.2f}%")
print(f"{p2:.2f}%")
print(f"{p3:.2f}%")
print(f"{p4:.2f}%")
print(f"{p5:.2f}%")

