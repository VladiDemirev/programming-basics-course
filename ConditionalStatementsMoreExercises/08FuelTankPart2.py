type_fuel = input()     # Diesel, Gasoline or Gas
quantity_fuel = float(input())
club_card = input()     # Yes or No

# OPTION 1

if club_card == "No":
    DIESEL_COST_LTR = 2.33
    GASOLINE_COST_LTR = 2.22
    GAS_COST_LTR = 0.93
elif club_card == "Yes":
    DIESEL_COST_LTR = 2.21
    GASOLINE_COST_LTR = 2.04
    GAS_COST_LTR = 0.85

if 20 <= quantity_fuel <= 25:
    discount_diesel = DIESEL_COST_LTR * 0.08
    discount_gasoline = GASOLINE_COST_LTR * 0.08
    discount_gas = GAS_COST_LTR * 0.08
elif quantity_fuel > 25:
    discount_diesel = DIESEL_COST_LTR * 0.1
    discount_gasoline = GASOLINE_COST_LTR * 0.1
    discount_gas = GAS_COST_LTR * 0.1
else:
    discount_diesel = 0
    discount_gasoline = 0
    discount_gas = 0

if type_fuel == "Diesel":
    final_fuel_cost = DIESEL_COST_LTR * quantity_fuel - discount_diesel * quantity_fuel
elif type_fuel == "Gasoline":
    final_fuel_cost = GASOLINE_COST_LTR * quantity_fuel - discount_gasoline * quantity_fuel
elif type_fuel == "Gas":
    final_fuel_cost = GAS_COST_LTR * quantity_fuel - discount_gas * quantity_fuel

print(f"{final_fuel_cost:.2f} lv.")

# OPTION 2

# DIESEL_COST_LTR = 2.33
# GASOLINE_COST_LTR = 2.22
# GAS_COST_LTR = 0.93
#
# DIESEL_COST_LTR_DISCOUNT = 2.33 - 0.12
# GASOLINE_COST_LTR_DISCOUNT = 2.22 - 0.18
# GAS_COST_LTR_DISCOUNT = 0.93 - 0.08
#
# final_fuel_cost = 0
#
# if club_card == "No":
#     if type_fuel == "Diesel":
#         if 20 <= quantity_fuel <= 25:
#             final_fuel_cost = (DIESEL_COST_LTR * quantity_fuel) - \
#                               ((DIESEL_COST_LTR * quantity_fuel) * 0.08)
#         elif quantity_fuel > 25:
#             final_fuel_cost = (DIESEL_COST_LTR * quantity_fuel) - \
#                               ((DIESEL_COST_LTR * quantity_fuel) * 0.1)
#         else:
#             final_fuel_cost = DIESEL_COST_LTR * quantity_fuel
#     if type_fuel == "Gasoline":
#         if 20 <= quantity_fuel <= 25:
#             final_fuel_cost = (GASOLINE_COST_LTR * quantity_fuel) - \
#                               ((GASOLINE_COST_LTR * quantity_fuel) * 0.08)
#         elif quantity_fuel > 25:
#             final_fuel_cost = (GASOLINE_COST_LTR * quantity_fuel) - \
#                               ((GASOLINE_COST_LTR * quantity_fuel) * 0.1)
#         else:
#             final_fuel_cost = GASOLINE_COST_LTR * quantity_fuel
#     if type_fuel == "Gas":
#         if 20 <= quantity_fuel <= 25:
#             final_fuel_cost = (GAS_COST_LTR * quantity_fuel) - \
#                               ((GAS_COST_LTR * quantity_fuel) * 0.08)
#         elif quantity_fuel > 25:
#             final_fuel_cost = (GAS_COST_LTR * quantity_fuel) - \
#                               ((GAS_COST_LTR * quantity_fuel) * 0.1)
#         else:
#             final_fuel_cost = GAS_COST_LTR * quantity_fuel
#
# if club_card == "Yes":
#     if type_fuel == "Diesel":
#         if 20 <= quantity_fuel <= 25:
#             final_fuel_cost = (DIESEL_COST_LTR_DISCOUNT * quantity_fuel) - \
#                               ((DIESEL_COST_LTR_DISCOUNT * quantity_fuel) * 0.08)
#         elif quantity_fuel > 25:
#             final_fuel_cost = (DIESEL_COST_LTR_DISCOUNT * quantity_fuel) - \
#                               ((DIESEL_COST_LTR_DISCOUNT * quantity_fuel) * 0.1)
#         else:
#             final_fuel_cost = DIESEL_COST_LTR_DISCOUNT * quantity_fuel
#     if type_fuel == "Gasoline":
#         if 20 <= quantity_fuel <= 25:
#             final_fuel_cost = (GASOLINE_COST_LTR_DISCOUNT * quantity_fuel) - \
#                               ((GASOLINE_COST_LTR_DISCOUNT * quantity_fuel) * 0.08)
#         elif quantity_fuel > 25:
#             final_fuel_cost = (GASOLINE_COST_LTR_DISCOUNT * quantity_fuel) - \
#                               ((GASOLINE_COST_LTR_DISCOUNT * quantity_fuel) * 0.1)
#         else:
#             final_fuel_cost = GASOLINE_COST_LTR_DISCOUNT * quantity_fuel
#     if type_fuel == "Gas":
#         if 20 <= quantity_fuel <= 25:
#             final_fuel_cost = (GAS_COST_LTR_DISCOUNT * quantity_fuel) - \
#                               ((GAS_COST_LTR_DISCOUNT * quantity_fuel) * 0.08)
#         elif quantity_fuel > 25:
#             final_fuel_cost = (GAS_COST_LTR_DISCOUNT * quantity_fuel) - \
#                               ((GAS_COST_LTR_DISCOUNT * quantity_fuel) * 0.1)
#         else:
#             final_fuel_cost = GAS_COST_LTR_DISCOUNT * quantity_fuel
#
# print(f"{final_fuel_cost:.2f} lv.")

