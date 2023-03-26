player1_eggs = int(input())
player2_eggs = int(input())

while player1_eggs > 0 and player2_eggs >0:
    user_input = input()

    if user_input == "End":
        break

    elif user_input == "one":
        player2_eggs -= 1
    else:
        player1_eggs -= 1

if player1_eggs <= 0:
    print(f"Player one is out of eggs. Player two has "
          f"{player2_eggs} eggs left.")
elif player2_eggs <= 0:
    print(f"Player two is out of eggs. Player one has "
          f"{player1_eggs} eggs left.")
else:
    print(f"Player one has {player1_eggs} eggs left.")
    print(f"Player two has {player2_eggs} eggs left.")
