import sys

count_number = int(input())

max_number = -sys.maxsize
sum_numbers = 0

for i in range(1, count_number+1):
    user_input = int(input())
    if user_input > max_number:
        max_number = user_input
    sum_numbers += user_input

if max_number == sum_numbers - max_number:
    print("Yes\n"f"Sum = {max_number}")
    # print(f"Sum = {max_number}")
else:
    print("No\n"f"Diff = {abs(max_number - (sum_numbers - max_number))}")
    # print(f"Diff = {abs(max_number - (sum_numbers - max_number))}")

