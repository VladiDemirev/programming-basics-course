days = int(input())
food = float(input())

biscuits = 0
eaten_food = 0
eaten_food_dog = 0
eaten_food_cat = 0

for i in range(1, days + 1):
    dog_food = 0
    cat_food = 0

    dog_food += int(input())
    eaten_food_dog += dog_food
    cat_food += int(input())
    eaten_food_cat += cat_food

    eaten_food += dog_food + cat_food

    if i % 3 == 0:
        biscuits += (dog_food + cat_food) * 0.1

print(f"Total eaten biscuits: {round(biscuits)}gr.")
print(f"{eaten_food / food * 100:.2f}% of the food has been eaten.")
print(f"{eaten_food_dog / eaten_food * 100:.2f}% eaten from the dog.")
print(f"{eaten_food_cat / eaten_food * 100:.2f}% eaten from the cat.")



