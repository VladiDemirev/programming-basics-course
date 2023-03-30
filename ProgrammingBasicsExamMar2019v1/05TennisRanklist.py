from math import floor

tournament_count = int(input())
starting_points = int(input())

points = 0
final_points = 0
average_points = 0
tournament_won = 0

for _ in range(tournament_count):
    stage = input()

    if stage == "W":
        points += 2000
        tournament_won += 1
    elif stage == "F":
        points += 1200
    else:
        points += 720

final_points = starting_points + points
average_points = points / tournament_count

print(f"Final points: {final_points}")
print(f"Average points: {floor(average_points)}")
print(f"{tournament_won / tournament_count * 100:.2f}%")