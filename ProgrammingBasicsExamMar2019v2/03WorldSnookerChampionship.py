stage = input()
ticket_type = input()
ticket_count = int(input())
picture = input()

ticket_cost = 0
total_cost = 0

if stage == "Quarter final":
    if ticket_type == "Standard":
        ticket_cost = 55.50
    elif ticket_type == "Premium":
        ticket_cost = 105.20
    else:
        ticket_cost = 118.90
elif stage == "Semi final":
    if ticket_type == "Standard":
        ticket_cost = 75.88
    elif ticket_type == "Premium":
        ticket_cost = 125.22
    else:
        ticket_cost = 300.40
else:
    if ticket_type == "Standard":
        ticket_cost = 110.10
    elif ticket_type == "Premium":
        ticket_cost = 160.66
    else:
        ticket_cost = 400

total_cost = ticket_cost * ticket_count

if total_cost <= 2500:
    if picture == "Y":
        total_cost += (ticket_count * 40)
elif 2500 < total_cost <= 4000:
    total_cost *= 0.90
    if picture == "Y":
        total_cost += (ticket_count * 40)
elif total_cost > 4000:
    total_cost *= 0.75

print(f"{total_cost:.2f}")
