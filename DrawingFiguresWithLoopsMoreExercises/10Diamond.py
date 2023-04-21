# user_input = int(input())
# dash_leftRight = int((user_input - 1) / 2)
# dash_mid = user_input - 2 * dash_leftRight - 2
#
# if user_input <= 2:
#     if dash_mid < 0:
#         print("-" * dash_leftRight + "*" + "-" * dash_leftRight)
#     else:
#         print("-" * dash_leftRight + "**" + "-" * dash_leftRight)
#
# if user_input > 2:
#     if dash_mid < 0:
#         print("-" * dash_leftRight + "*" + "-" * dash_leftRight)
#     else:
#         print("-" * dash_leftRight + "**" + "-" * dash_leftRight)
#
#     for row in range(int(user_input)):
#         if 0 < row < int((user_input - 1) / 2):
#             print("-" * (dash_leftRight - row) + "*" + "-" * (dash_mid + row * 2)
#                   + "*" + "-" * (dash_leftRight - row))
#         elif row == int((user_input - 1) / 2):
#             print("-" * (dash_leftRight - row) + "*" + "-" * (user_input - 2)
#                   + "*" + "-" * (dash_leftRight - row))
#         elif int((user_input - 1) / 2) < row < (user_input - 1):
#             print("-" * (abs(dash_leftRight - row)) + "*" + "-"
#                   * abs(user_input - 2 - abs((2 * dash_leftRight - 2 * row)))
#                   + "*" + "-" * (abs(dash_leftRight - row)))
#
#     if dash_mid < 0:
#         print("-" * dash_leftRight + "*" + "-" * dash_leftRight)

max_col = int(input())
rows = (max_col - 1) if max_col % 2 == 0 else max_col - 2
first_row_stars = 2 if max_col % 2 == 0 else 1
data = []

data.append("*" * first_row_stars)
if max_col > 2:
    for r in range((1 + (max_col % 2 == 0)), rows * 2 + 1, 2):
        if r <= rows:
            data.append("*" + ("-" * r) + "*")
        else:
            data.append("*" + ("-" * ((rows - abs(rows - r)) + (2 if max_col % 2 == 0 else 0))) + "*")
    data.append("*" * first_row_stars)
    data = [r.center(max_col, "-") for r in data]

print(*data, sep="\n")
