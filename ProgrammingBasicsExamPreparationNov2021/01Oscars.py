hall_rent = int(input())

cost_figures = hall_rent * 0.7
cost_catering = cost_figures * 0.85
cost_sound = cost_catering * 0.5

total_costs = hall_rent + cost_figures + cost_catering + cost_sound

print(f"{total_costs:.2f}")
