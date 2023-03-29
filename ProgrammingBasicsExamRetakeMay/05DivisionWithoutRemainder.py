n = int(input())

division_2 = 0
division_3 = 0
division_4 = 0

p1 = 0
p2 = 0
p3 = 0

for _ in range(n):
    number = int(input())

    if number % 2 == 0:
        division_2 += 1
    if number % 3 == 0:
        division_3 += 1
    if number % 4 == 0:
        division_4 += 1

p1 = division_2 / n * 100
p2 = division_3 / n * 100
p3 = division_4 / n * 100

print(f"{p1:.2f}%\n{p2:.2f}%\n{p3:.2f}%")