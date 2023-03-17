# OPTION 1

from sys import maxsize

max_diff = -maxsize
last_sum = -maxsize

for index in range(int(input())):
    num1 = int(input())
    num2 = int(input())

    current_pairs_sum = num1 + num2

    if index == 0:
        last_sum = current_pairs_sum

    if last_sum != current_pairs_sum:
        if abs(current_pairs_sum - last_sum) > max_diff:
            max_diff = current_pairs_sum - last_sum

        last_sum = current_pairs_sum

if max_diff == -maxsize:
    print(f"Yes, value ={last_sum}")
else:
    print(f"No, maxdiff={max_diff}")

# OPTION 2

# count_numbers = int(input())
#
# result = []
# sum = 0
# difference = []
# max_diff = 0
#
# for i in range(1, count_numbers * 2 + 1):
#     num = int(input())
#     sum += num
#     if i % 2 ==0:
#         result += [sum]
#         sum = 0
#
# for j in range(1, len(result)):
#     diff = abs(result[j] - result[j - 1])
#     difference += [diff]
#     max_diff = max(max_diff, diff)
#
# if max_diff == 0:
#     print(f"Yes, value={result[0]}")
# else:
#     print(f"No, maxdiff={max_diff}")

