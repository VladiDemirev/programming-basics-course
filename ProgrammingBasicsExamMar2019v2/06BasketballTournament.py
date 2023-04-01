won_games = 0
lost_games = 0

while True:
    current_game = 0
    total_games = won_games + lost_games

    user_input = input()

    if user_input == "End of tournaments":
        print(f"{won_games / total_games * 100:.2f}% matches win")
        print(f"{lost_games / total_games * 100:.2f}% matches lost")
        break

    games = int(input())

    for _ in range(games):
        current_game += 1
        user_team = int(input())
        other_team = int(input())

        if user_team > other_team:
            print(f"Game {current_game} of tournament {user_input}: "
                  f"win with {user_team - other_team} points.")
            won_games += 1
        else:
            print(f"Game {current_game} of tournament {user_input}: "
                  f"lost with {other_team - user_team} points.")
            lost_games += 1