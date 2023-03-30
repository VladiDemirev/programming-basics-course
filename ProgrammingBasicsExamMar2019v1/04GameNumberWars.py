first_player = input()
second_player = input()

points1 = 0
points2 = 0

while True:
    user_input1 = input()

    if user_input1 == "End of game":
        print(f"{first_player} has {points1} points")
        print(f"{second_player} has {points2} points")
        break

    else:
        user_input1 = int(user_input1)

    user_input2 = int(input())

    if user_input1 > user_input2:
        points1 += (user_input1 - user_input2)
    elif user_input1 < user_input2:
        points2 += (user_input2 - user_input1)

    elif user_input1 == user_input2:
        user_input1 = int(input())
        user_input2 = int(input())
        print("Number wars!")
        if user_input1 > user_input2:
            print(f"{first_player} is winner with {points1} points")
        else:
            print(f"{second_player} is winner with {points2} points")
        break
