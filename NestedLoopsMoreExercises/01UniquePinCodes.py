upper_num1 = int(input())
upper_num2 = int(input())
upper_num3 = int(input())

pin = []

for i in range(1, upper_num1 + 1):
    for j in range(1, upper_num2 + 1):
        for k in range(1, upper_num3 + 1):
            if i % 2 == 0 and (j == 2 or j == 3 or j == 5 or j == 7) and k % 2 == 0:
                pin.extend([i, j, k])

                print(*pin)
                pin.clear()



