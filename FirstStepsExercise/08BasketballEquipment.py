annual_tax = int(input())

sneakers = annual_tax - annual_tax * 40 / 100
kit = sneakers - sneakers * 20 / 100
ball = kit * 1 / 4
accessory = ball * 1 / 5

expenses = annual_tax + sneakers + kit + ball + accessory

print(expenses)