first_game = input()
second_game = input()
third_game = input()

won = 0
lost = 0
draw = 0

if first_game[0] > first_game[2]:
    won += 1
elif first_game[0] < first_game[2]:
    lost += 1
else:
    draw += 1

if second_game[0] > second_game[2]:
    won += 1
elif second_game[0] < second_game[2]:
    lost += 1
else:
    draw += 1

if third_game[0] > third_game[2]:
    won += 1
elif third_game[0] < third_game[2]:
    lost += 1
else:
    draw += 1

print(f"Team won {won} games.")
print(f"Team lost {lost} games.")
print(f"Drawn games: {draw}")