import sys

count_numbers = int(input())

lowest_number = -sys.maxsize
highest_number = sys.maxsize

for number in range(0, count_numbers):
    user_input = int(input())
    if user_input > lowest_number:
        lowest_number = user_input
    if user_input < highest_number:
        highest_number = user_input

print(f"Max number: {lowest_number}")
print(f"Min number: {highest_number}")