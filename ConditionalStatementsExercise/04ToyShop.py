PUZZLE = 2.60
DOLL = 3
BEAR = 4.10
MINION = 8.20
TRUCK = 2

holiday = float(input())
num_puzzles = int(input())
num_dolls = int(input())
num_bears = int(input())
num_minions = int(input())
num_trucks = int(input())

order = num_puzzles + num_dolls + num_bears + num_minions + num_trucks

earnings = PUZZLE * num_puzzles + DOLL * num_dolls + BEAR * num_bears \
           + MINION * num_minions + TRUCK * num_trucks

if order >= 50:
    earnings = earnings - (earnings * 25 / 100)

if earnings >= holiday:
    print("Yes! {:.2f} lv left.".format(earnings - earnings * 10 / 100
                                        - holiday))
else:
    print("Not enough money! {:.2f} lv needed.".format(holiday - (earnings
                                                       - earnings * 10 / 100)))
