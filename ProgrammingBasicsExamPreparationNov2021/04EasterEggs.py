num_painted_eggs = int(input())

egg_color = None

num_red_eggs = 0
num_orange_eggs = 0
num_blue_eggs = 0
num_green_eggs = 0

max_eggs_color = None

for _ in range(num_painted_eggs):
    egg_color = input()

    if egg_color == "red":
        num_red_eggs += 1
    elif egg_color == "orange":
        num_orange_eggs += 1
    elif egg_color == "blue":
        num_blue_eggs += 1
    else:
        num_green_eggs += 1

if max(num_red_eggs, num_orange_eggs, num_blue_eggs, num_green_eggs) == num_red_eggs:
    max_eggs_color = "red"
elif max(num_red_eggs, num_orange_eggs, num_blue_eggs, num_green_eggs) == num_orange_eggs:
    max_eggs_color = "orange"
elif max(num_red_eggs, num_orange_eggs, num_blue_eggs, num_green_eggs) == num_blue_eggs:
    max_eggs_color = "blue"
else:
    max_eggs_color = "green"

print(f"Red eggs: {num_red_eggs}")
print(f"Orange eggs: {num_orange_eggs}")
print(f"Blue eggs: {num_blue_eggs}")
print(f"Green eggs: {num_green_eggs}")
print(f"Max eggs: "
      f"{max(num_red_eggs, num_orange_eggs, num_blue_eggs, num_green_eggs)}"
      f" -> {max_eggs_color}")
