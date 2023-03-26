painted_eggs_count = int(input())

red_eggs = 0
orange_eggs = 0
blue_eggs = 0
green_eggs = 0

max_eggs = 0
max_eggs_color = None

while painted_eggs_count > 0:
    egg_color = input()
    painted_eggs_count -= 1

    if egg_color == "red":
        red_eggs += 1
    elif egg_color == "orange":
        orange_eggs += 1
    elif egg_color == "blue":
        blue_eggs += 1
    else:
        green_eggs += 1

# max_eggs = max(red_eggs, orange_eggs, blue_eggs, green_eggs)

if red_eggs > orange_eggs and red_eggs > blue_eggs and red_eggs > green_eggs:
    max_eggs = red_eggs
    max_eggs_color = "red"
elif orange_eggs > red_eggs and orange_eggs > blue_eggs and orange_eggs > green_eggs:
    max_eggs = orange_eggs
    max_eggs_color = "orange"
elif blue_eggs > red_eggs and blue_eggs > orange_eggs and blue_eggs > green_eggs:
    max_eggs = blue_eggs
    max_eggs_color = "blue"
elif green_eggs > red_eggs and green_eggs > orange_eggs and green_eggs > blue_eggs:
    max_eggs = green_eggs
    max_eggs_color = "green"

print(f"Red eggs: {red_eggs}")
print(f"Orange eggs: {orange_eggs}")
print(f"Blue eggs: {blue_eggs}")
print(f"Green eggs: {green_eggs}")
print(f"Max eggs: {max_eggs} -> {max_eggs_color}")
