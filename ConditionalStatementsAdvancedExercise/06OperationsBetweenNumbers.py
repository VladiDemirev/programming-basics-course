N1 = int(input())
N2 = int(input())
operator = input()

result = None

# OPTION 1

if operator == "+":
    result = f"{N1} {operator} {N2} = {N1 + N2}" + (" - even" if (N1 + N2) % 2 == 0 else " - odd")
elif operator == "-":
    result = f"{N1} {operator} {N2} = {N1 - N2}" + (" - even" if (N1 - N2) % 2 == 0 else " - odd")
elif operator == "*":
    result = f"{N1} {operator} {N2} = {N1 * N2}" + (" - even" if (N1 * N2) % 2 == 0 else " - odd")
elif N2 == 0:
    result = f"Cannot divide {N1} by zero"
elif operator == "/":
    result = f"{N1} {operator} {N2} = {N1 / N2:.2f}"
elif operator == "%":
    result = f"{N1} {operator} {N2} = {N1 % N2}"

print(result)

# OPTION 2

# if operator == "+":
#     result = N1 + N2
# elif operator == "-":
#     result = N1 - N2
# elif operator == "*":
#     result = N1 * N2
# elif operator == "/":
#     if N2 == 0:
#         print(f"Cannot divide {N1} by zero")
#     else:
#         result = N1 / N2
#         print(f"{N1} {operator} {N2} = {result:.2f}")
# elif operator == "%":
#     if N2 == 0:
#         print(f"Cannot divide {N1} by zero")
#     else:
#         result = N1 % N2
#         print(f"{N1} {operator} {N2} = {result}")
#
# if operator == "+" or operator == "-" or operator == "*":
#     if result % 2 == 0:
#         print(f"{N1} {operator} {N2} = {result} - even")
#     else:
#         print(f"{N1} {operator} {N2} = {result} - odd")




