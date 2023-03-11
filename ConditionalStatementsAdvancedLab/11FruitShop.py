fruit = input()
day = input()
quantity = float(input())

total_price = 0

day_list = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
weekend_list = ["Saturday", "Sunday"]
fruit_list = ["banana", "apple", "orange", "grapefruit", "kiwi", "pineapple",
              "grapes"]

# correct_input = True

if fruit == "banana":
    if day in day_list:
        total_price = 2.50 * quantity
    elif day in weekend_list:
        total_price = 2.70 * quantity
elif fruit == "apple":
    if day in day_list:
        total_price = 1.20 * quantity
    elif day in weekend_list:
        total_price = 1.25 * quantity
elif fruit == "orange":
    if day in day_list:
        total_price = 0.85 * quantity
    elif day in weekend_list:
        total_price = 0.90 * quantity
elif fruit == "grapefruit":
    if day in day_list:
        total_price = 1.45 * quantity
    elif day in weekend_list:
        total_price = 1.60 * quantity
elif fruit == "kiwi":
    if day in day_list:
        total_price = 2.70 * quantity
    elif day in weekend_list:
        total_price = 3.00 * quantity
elif fruit == "pineapple":
    if day in day_list:
        total_price = 5.50 * quantity
    elif day in weekend_list:
        total_price = 5.60 * quantity
elif fruit == "grapes":
    if day in day_list:
        total_price = 3.85 * quantity
    elif day in weekend_list:
        total_price = 4.20 * quantity
# else:
#     correct_input = False

if (day not in day_list and day not in weekend_list) or fruit \
        not in fruit_list:
    print("error")
else:
    print(f"{total_price:.2f}")