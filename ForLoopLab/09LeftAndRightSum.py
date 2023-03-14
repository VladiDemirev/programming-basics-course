count_numbers = int(input())

sum_left_numbers = 0
sum_right_numbers = 0

for i in range(0, 2 * count_numbers):
    if i in range (0, count_numbers):
        user_input = int(input())
        sum_left_numbers += user_input
    if i in range (count_numbers, 2 * count_numbers):
        user_input = int(input())
        sum_right_numbers += user_input

if sum_left_numbers == sum_right_numbers:
    print(f"Yes, sum = {sum_left_numbers}")
else:
    print(f"No, diff = {abs(sum_left_numbers - sum_right_numbers)}")

# OPTION 2

# n = int(input())
# left_sum = 0
# for i in range(1, n + 1):
#     left_sum = left_sum + int(input())
#
# right_sum = 0
# for i in range(1, n + 1):
#     right_sum = right_sum + int(input())
#
# if left_sum == right_sum:
#     print(f"Yes, sum = {left_sum}")
# else:
#     diff = abs(right_sum - left_sum)
#     print(f"No, diff = {diff}")

