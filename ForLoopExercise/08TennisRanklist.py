import math
from math import floor, ceil

num_tournaments = int(input())
starting_points = int(input())

points_tournament = 0
won_tournaments = 0

for i in range(0, num_tournaments):
    tournament_stage = input()
    if tournament_stage == "W":
        points_tournament += 2000
        won_tournaments += 1
    elif tournament_stage == "F":
        points_tournament += 1200
    elif tournament_stage == "SF":
        points_tournament += 720

print(f"Final points: {starting_points + points_tournament}")
print(f"Average points: {floor(points_tournament / num_tournaments)}")
print(f"{won_tournaments / num_tournaments *100:.2f}%")
