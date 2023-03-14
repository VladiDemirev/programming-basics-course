count_number = int(input())

sum_even_position_number = 0
sum_odd_position_number = 0

for i in range(1, count_number+1):
    if i in range(1, count_number+1, 2):
        user_input = int(input())
        sum_odd_position_number += user_input
    if i in range(2, count_number+1, 2):
        user_input = int(input())
        sum_even_position_number += user_input

if sum_odd_position_number == sum_even_position_number:
    print("Yes")
    print(f"Sum = {sum_odd_position_number}")
else:
    print("No")
    print(f"Diff = {abs(sum_odd_position_number - sum_even_position_number)}")

# OPTION 2

# n = int(input())
# odd_sum = 0
# even_sum = 0
# for i in range(1, n + 1):
#     element = int(input())
#     if i % 2 == 0:
#         even_sum += element
#     else:
#         odd_sum += element
# TODO: print the sum / difference

