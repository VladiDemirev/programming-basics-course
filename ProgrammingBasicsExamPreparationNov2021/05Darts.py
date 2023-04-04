# OPTION 1

player_name = input()
STARTING_POINTS = 301
is_retired = False
successful_shots = 0
unsuccessful_shots = 0

while True:
    sector = input()

    if sector == "Retire":
        is_retired = True
        break

    if sector == "Single":
        points = int(input())
        STARTING_POINTS -= points
    elif sector == "Double":
        points = int(input()) * 2
        STARTING_POINTS -= points
    else:
        points = int(input()) * 3
        STARTING_POINTS -= points

    if STARTING_POINTS < 0:
        unsuccessful_shots += 1
        STARTING_POINTS += points
        continue

    successful_shots += 1

    if STARTING_POINTS <= 0:
        break

if is_retired:
    print(f"{player_name} retired after {unsuccessful_shots} unsuccessful shots.")
else:
    print(f"{player_name} won the leg with {successful_shots} shots.")

# OPTION 2

# player_name = input()
# STARTING_POINTS = 301
# is_retired = False
# successful_shots = 0
# unsuccessful_shots = 0
# hit_points = 0
#
# while True:
#     sector = input()
#
#     if sector == "Retire":
#         is_retired = True
#         break
#
#     points = int(input())
#
#     if sector == "Single":
#         STARTING_POINTS -= points
#         hit_points = points
#     elif sector == "Double":
#         STARTING_POINTS -= (points * 2)
#         hit_points = points * 2
#     else:
#         STARTING_POINTS -= (points * 3)
#         hit_points = points * 3
#
#     if STARTING_POINTS < 0:
#         unsuccessful_shots += 1
#         STARTING_POINTS += hit_points
#         continue
#
#     successful_shots += 1
#
#     if STARTING_POINTS <= 0:
#         break
#
# if is_retired:
#     print(f"{player_name} retired after {unsuccessful_shots} unsuccessful shots.")
# else:
#     print(f"{player_name} won the leg with {successful_shots} shots.")



