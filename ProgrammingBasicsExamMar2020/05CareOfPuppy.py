food = int(input()) * 1000
eaten_food = 0

while True:
    user_input = input()

    if user_input == "Adopted":
        break
    else:
        eaten_food += int(user_input)

if food >= eaten_food:
    print(f"Food is enough! Leftovers: {food - eaten_food} grams.")
else:
    print(f"Food is not enough. You need {eaten_food - food} grams more.")

