cost_strawberry = float(input())
qtty_bananas = float(input())
qtty_oranges = float(input())
qtty_raspberries = float(input())
qtty_strawberries = float(input())
cost_raspberries = cost_strawberry / 2
cost_oranges = cost_raspberries * 0.6
cost_bananas = cost_raspberries * 0.2

total_cost = cost_strawberry * qtty_strawberries + cost_bananas * qtty_bananas + cost_oranges * qtty_oranges + cost_raspberries *  qtty_raspberries

print(f"{total_cost:.2f}")
