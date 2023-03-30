from math import floor, ceil

cost_racket = float(input())
count_rackets = int(input())
count_sneakers = int(input())
cost_sneakers = cost_racket / 6

total_cost = cost_racket * count_rackets + cost_sneakers * count_sneakers
other_equipment = total_cost * 0.2
final_cost = total_cost + other_equipment

print(f"Price to be paid by Djokovic {floor(final_cost / 8)}")
print(f"Price to be paid by sponsors {ceil(final_cost * (7 / 8))}")

