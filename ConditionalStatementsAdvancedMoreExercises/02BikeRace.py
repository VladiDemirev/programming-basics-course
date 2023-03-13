num_juniors_bikers = int(input())
num_seniors_bikers = int(input())
track_type = input()

JUNIORS_TAX = 0
SENIORS_TAX = 0

if track_type == "trail":
    JUNIORS_TAX = 5.50
    SENIORS_TAX = 7
elif track_type == "cross-country":
    JUNIORS_TAX = 8
    SENIORS_TAX = 9.50
    if (num_juniors_bikers + num_seniors_bikers) >= 50:
        JUNIORS_TAX = JUNIORS_TAX - JUNIORS_TAX * 0.25
        SENIORS_TAX = SENIORS_TAX - SENIORS_TAX * 0.25
elif track_type == "downhill":
    JUNIORS_TAX = 12.25
    SENIORS_TAX = 13.75
elif track_type == "road":
    JUNIORS_TAX = 20
    SENIORS_TAX = 21.50

gross_ticket_earnings = num_juniors_bikers * JUNIORS_TAX + num_seniors_bikers \
                  * SENIORS_TAX
expenses_cost = gross_ticket_earnings * 0.05
net_ticket_earning = gross_ticket_earnings - expenses_cost

print(f"{net_ticket_earning:.2f}")