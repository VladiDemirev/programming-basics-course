contract_duration = input()
contract_type = input()
added_internet = input()
months = int(input())

cost = 0

if contract_duration == "one":
    if contract_type == "Small":
        cost = 9.98
    elif contract_type == "Middle":
        cost = 18.99
    elif contract_type == "Large":
        cost = 25.98
    else:
        cost = 35.99

else:
    if contract_type == "Small":
        cost = 8.58
    elif contract_type == "Middle":
        cost = 17.09
    elif contract_type == "Large":
        cost = 23.59
    else:
        cost = 31.79

if added_internet == "yes":
    if cost <= 10:
        cost += 5.50
    elif 10 < cost <= 30:
        cost += 4.35
    else:
        cost += 3.85

if contract_duration == "one":
    cost *= months
else:
    cost *= months * 0.9625

print(f"{cost:.2f} lv.")