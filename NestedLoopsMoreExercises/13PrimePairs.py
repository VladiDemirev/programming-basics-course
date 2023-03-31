# OPTION 1

start_value_first_pair = int(input())
start_value_second_pair = int(input())
diff_start_end_first_pair = int(input())
diff_start_end_second_pair = int(input())

end_value_first_pair = diff_start_end_first_pair + start_value_first_pair
end_value_second_pair = diff_start_end_second_pair + start_value_second_pair

first_pair_num = 0
second_pair_num = 0

for first_pair in range(start_value_first_pair, end_value_first_pair + 1):
    for i in range(2, first_pair):
        if first_pair % i == 0:
            break
    else:
        first_pair_num = first_pair
        for second_pair in range(start_value_second_pair, end_value_second_pair + 1):
            for j in range(2, second_pair):
                if second_pair % j == 0:
                    break
            else:
                second_pair_num = second_pair
                print(f"{first_pair_num}{second_pair_num}")

# OPTION 2

# start_value_first_pair = int(input())
# start_value_second_pair = int(input())
# diff_start_end_first_pair = int(input())
# diff_start_end_second_pair = int(input())
#
# end_value_first_pair = diff_start_end_first_pair + start_value_first_pair
# end_value_second_pair = diff_start_end_second_pair + start_value_second_pair

#
# def is_prime(n):
#   if n <= 1:
#     return False
#
#   for i in range(2, n):
#     if n % i == 0:
#       return False
#
#   return True

#
# for first_pair in range(start_value_first_pair, end_value_first_pair + 1):
#   for second_pair in range(start_value_second_pair, end_value_second_pair + 1):
#     if (
#       is_prime(first_pair) and
#       is_prime(second_pair)
#     ):
#       print(f"{first_pair}{second_pair}")

