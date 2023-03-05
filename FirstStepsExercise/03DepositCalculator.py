deposit = float(input())
period = int(input())
interest = float(input())

sum_amount = deposit + period * ((deposit * interest/100) / 12)

print(sum_amount)