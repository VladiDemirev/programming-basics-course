joinery_count = int(input())
joinery_type = input()
delivery_option = input()

DELIVERY_COST = 60
unit_cost = 0
order_cost = 0

if joinery_type == "90X130":
    unit_cost = 110

    if 30 < joinery_count <= 60:
        unit_cost *= 0.95
    elif joinery_count > 60:
        unit_cost *= 0.92

elif joinery_type == "100X150":
    unit_cost = 140

    if 40 < joinery_count <= 80:
        unit_cost *= 0.94
    elif joinery_count > 80:
        unit_cost *= 0.9

elif joinery_type == "130X180":
    unit_cost = 190

    if 20 < joinery_count <= 50:
        unit_cost *= 0.93
    elif joinery_count > 50:
        unit_cost *= 0.88

else:
    unit_cost = 250

    if 25 < joinery_count <= 50:
        unit_cost *= 0.91
    elif joinery_count > 50:
        unit_cost *= 0.86

order_cost = unit_cost * joinery_count

if delivery_option == "With delivery":
    total_order_cost = order_cost + DELIVERY_COST
else:
    total_order_cost = order_cost

if joinery_count > 99:
    total_order_cost *= 0.96

if joinery_count < 10:
    print("Invalid order")
else:
    print(f"{total_order_cost:.2f} BGN")
