type_fuel = input()     # choose between Diesel, Gasoline and Gas
liters_in_tank = float(input())

if type_fuel == "Diesel" or type_fuel == "Gasoline" or type_fuel == "Gas":
    if liters_in_tank >= 25:
        print(f"You have enough {type_fuel.lower()}.")
    if liters_in_tank < 25:
        print(f"Fill your tank with {type_fuel.lower()}!")
else:
    print("Invalid fuel!")
