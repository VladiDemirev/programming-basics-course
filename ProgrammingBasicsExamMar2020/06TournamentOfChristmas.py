tournament_duration = int(input())

total_raised_money = 0
total_won = 0
total_lost = 0

for _ in range(tournament_duration):
    won_games = 0
    lost_games = 0
    raised_money = 0

    while True:
        user_input = input()

        if user_input == "Finish":
            break

        result = input()

        if result == "win":
            raised_money += 20
            won_games += 1
            total_won += 1
        else:
            lost_games += 1
            total_lost += 1

    if won_games > lost_games:
        raised_money *= 1.10

    total_raised_money += raised_money

if total_won > total_lost:
    total_raised_money *= 1.20
    print(f"You won the tournament! Total raised money: {total_raised_money:.2f}")
else:
    print(f"You lost the tournament! Total raised money: {total_raised_money:.2f}")




