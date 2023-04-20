user_input = int(input())
num_stars = 0

for i in range(int((user_input + 1) / 2)):
    if i == 0 and user_input % 2 != 0:
        print("-" * int((user_input - 1) / 2) + "*" + "-" * int((user_input - 1) / 2))
    elif i == 0 and user_input % 2 == 0:
        print("-" * int((user_input - 2) / 2) + "**" + "-" * int((user_input - 2) / 2))
    if i > 0 and user_input % 2 != 0:
        num_stars = int(i * 2 + 1)
        if num_stars < user_input:
            print(
                "-" * (int((user_input - num_stars) / 2)) + "*" * num_stars + "-" * (int((user_input - num_stars) / 2)))
        else:
            print("*" * num_stars)
    elif i > 0 and user_input % 2 == 0:
        num_stars = int(i * 2 + 2)
        if num_stars < user_input:
            print(
                "-" * (int((user_input - num_stars) / 2)) + "*" * num_stars + "-" * (int((user_input - num_stars) / 2)))
        else:
            print("*" * num_stars)

for j in range(1, int(user_input / 2 + 1)):
    print("|" + "*" * int(user_input - 2) + "|")
