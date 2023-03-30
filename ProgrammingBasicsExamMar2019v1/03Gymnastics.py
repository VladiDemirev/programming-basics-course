country = input()
equipment = input()

score = 0
remaining_points = 0

if equipment == "ribbon":
    if country == "Russia":
        difficulty = 9.100
        performance = 9.400
    elif country == "Bulgaria":
        difficulty = 9.600
        performance = 9.400
    elif country == "Italy":
        difficulty = 9.200
        performance = 9.500

elif equipment == "hoop":
    if country == "Russia":
        difficulty = 9.300
        performance = 9.800
    elif country == "Bulgaria":
        difficulty = 9.550
        performance = 9.750
    elif country == "Italy":
        difficulty = 9.450
        performance = 9.350

else:
    if country == "Russia":
        difficulty = 9.600
        performance = 9.000
    elif country == "Bulgaria":
        difficulty = 9.500
        performance = 9.400
    elif country == "Italy":
        difficulty = 9.700
        performance = 9.150

score = difficulty + performance
remaining_points = 20 - score

print(f"The team of {country} get {score:.3f} on {equipment}.")
print(f"{remaining_points / 20 * 100:.2f}%")