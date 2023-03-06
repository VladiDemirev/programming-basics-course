price_kg_vegetables = float(input())
price_kg_fruits = float(input())
total_kg_vegetables = int(input())
total_kg_fruits = int(input())

EURO_BGN_RATE = 1.94

income_lv = (price_kg_vegetables * total_kg_vegetables) + \
            (price_kg_fruits * total_kg_fruits)

income_eur = income_lv / EURO_BGN_RATE

print(f"{income_eur:.2f}")

