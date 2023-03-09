age = float(input())
sex = input()

if sex == "m":
    if age >= 16:
        print("Mr.")
    else:
        print("Master")

if sex == "f":
    if age >= 16:
        print("Ms.")
    else:
        print("Miss")

# if sex == "m" and age >= 16:
#     print("Mr.")
# elif sex == "m" and age < 16:
#     print("Master")
# elif sex == "f" and age >= 16:
#     print("Ms.")
# elif sex == "f" and age < 16:
#     print("Miss")