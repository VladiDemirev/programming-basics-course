food_bought = int(input()) * 1000
food_eaten = 0

while True:
    user_input = input()

    if user_input == "Adopted":
        break
    else:
        user_input = int(user_input)

    food_eaten += user_input

if food_bought >= food_eaten:
    print(f"Food is enough! Leftovers: {food_bought - food_eaten} grams.")
else:
    print(f"Food is not enough. You need {food_eaten - food_bought} grams more.")

