airline = input()
senior_tickets = int(input())
kid_tickets = int(input())
net_cost_senior_ticket = float(input())
service_fee = float(input())

net_cost_kid_ticket = net_cost_senior_ticket * 0.3

total_ticket_cost = (senior_tickets * (net_cost_senior_ticket + service_fee)) \
    + (kid_tickets * (net_cost_kid_ticket + service_fee))

agency_income = total_ticket_cost * 0.2

print(f"The profit of your agency from {airline} "
      f"tickets is {agency_income:.2f} lv.")