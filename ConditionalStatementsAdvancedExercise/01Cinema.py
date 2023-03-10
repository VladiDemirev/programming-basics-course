PREMIERE_TICKET = 12
NORMAL_TICKET = 7.50
DISCOUNT_TICKET = 5.00

type_ticket = input()
num_rows = int(input())
num_colons = int(input())

earnings = 0

full_theater = num_rows * num_colons

if type_ticket == "Premiere":
    earnings = full_theater * PREMIERE_TICKET
elif type_ticket == "Normal":
    earnings = full_theater * NORMAL_TICKET
elif type_ticket == "Discount":
    earnings = full_theater * DISCOUNT_TICKET

print(f"{earnings:.2f} leva")