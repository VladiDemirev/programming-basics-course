annual_tax = int(input())

sneakers_cost = annual_tax * 0.6
kit_cost = sneakers_cost * 0.8
ball_cost = kit_cost / 4
accessories_cost = ball_cost / 5

expenses = annual_tax + sneakers_cost + kit_cost + ball_cost + accessories_cost

print(f"{expenses:.2f}")

