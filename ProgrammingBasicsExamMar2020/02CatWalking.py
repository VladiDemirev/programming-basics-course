minutes = int(input())
walks = int(input())
calories = int(input())

total_calories = walks * minutes * 5

if total_calories >= calories * 0.5:
    print(f"Yes, the walk for your cat is enough. Burned calories per day: {total_calories}.")
else:
    print(f"No, the walk for your cat is not enough. Burned calories per day: {total_calories}.")