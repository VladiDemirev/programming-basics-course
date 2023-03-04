square_meters = float(input())

PRICE_SQUARE_METER = 7.61

final_price = square_meters * PRICE_SQUARE_METER

discount = final_price * 18 / 100

discounted_final_price = final_price - discount

print(f"The final price is: {discounted_final_price} lv.")
print(f"The discount is: {discount} lv.")