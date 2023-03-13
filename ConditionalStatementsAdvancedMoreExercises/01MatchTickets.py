budget = float(input())
category = input()
num_people = int(input())

ticket_cost = 0

if category == "VIP":
    ticket_cost = 499.99
elif category == "Normal":
    ticket_cost = 249.99

if 0 < num_people <= 4:
    transport_cost = budget * 0.75
elif 5 <= num_people <= 9:
    transport_cost = budget * 0.60
elif 10 <= num_people <= 24:
    transport_cost = budget * 0.50
elif 25 <= num_people <= 49:
    transport_cost = budget * 0.40
else:
    transport_cost = budget * 0.25

final_cost = ticket_cost * num_people + transport_cost

if budget >= final_cost:
    print(f"Yes! You have {(budget - final_cost):.2f} leva left.")
else:
    print(f"Not enough money! You need {(final_cost - budget):.2f} leva.")


