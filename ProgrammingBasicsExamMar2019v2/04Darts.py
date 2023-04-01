player = input()
start_points = 301
successful = 0
failed = 0

while start_points > 0:
    field = input()

    if field == "Retire":
        print(f"{player} retired after {failed} unsuccessful shots.")
        break

    points = int(input())

    if field == "Double":
        points *= 2
    elif field == "Triple":
        points *= 3

    start_points -= points

    if start_points < 0:
        failed += 1
        start_points += points
    else:
        successful += 1

if start_points == 0:
    print(f"{player} won the leg with {successful} shots.")




