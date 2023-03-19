num1 = int(input())
num2 = int(input())

even_sum = 0
odd_sum = 0

for i in range(num1, num2 + 1):
    number_to_str = str(i)
    for j, digit in enumerate(number_to_str):
        if j % 2 == 0:
            odd_sum += int(digit)
        else:
            even_sum += int(digit)
    if odd_sum == even_sum:
        print(i, end=" ")
    even_sum = 0
    odd_sum = 0