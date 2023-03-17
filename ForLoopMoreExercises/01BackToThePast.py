inherited_money = float(input())
year_to_live_until = int(input())

money_spent = 0

person_age = 17

for year in range(1800, year_to_live_until + 1):
    person_age += 1
    if year % 2 == 0:
        money_spent += 12000
    else:
        money_spent += (12000 + 50 * person_age)

if inherited_money >= money_spent:
    print(f"Yes! He will live a carefree life and will have "
          f"{abs(inherited_money - money_spent):.2f} dollars left.")
else:
    print(f"He will need "
          f"{abs(inherited_money - money_spent):.2f} dollars to survive.")