num_N = int(input())
num_M = int(input())
num_S = int(input())

for number in range(num_M, num_N - 1, -1):
    if number % 2 == 0 and number % 3 == 0:
        if number == num_S:
            break
        else:
            print(number, end=" ")

