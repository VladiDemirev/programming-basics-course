one_lv_coin = int(input())
two_lv_coin = int(input())
five_lv_coin = int(input())
amount = int(input())

for num1 in range(one_lv_coin + 1):
    payment1 = num1 * 1
    for num2 in range(two_lv_coin + 1):
        payment2 = num2 * 2
        for num5 in range(five_lv_coin + 1):
            payment3 = num5 * 5

            if payment1 + payment2 + payment3 == amount:
                print(f"{num1} * 1 lv. + {num2} * 2 lv. + {num5} * 5 lv. = {amount} lv.")
