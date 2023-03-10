month = input()
num_stays = int(input())

cost_stay_apartment = 0
cost_stay_studio = 0

if month == "May" or month == "October":
    cost_stay_studio = 50 * num_stays
    cost_stay_apartment = 65 * num_stays
    if 7 < num_stays <= 14:
        cost_stay_studio *= 0.95
    elif num_stays > 14:
        cost_stay_studio *= 0.7

elif month == "June" or month == "September":
    cost_stay_studio = 75.20 * num_stays
    cost_stay_apartment = 68.70 * num_stays
    if num_stays > 14:
        cost_stay_studio *= 0.8

elif month == "July" or month == "August":
    cost_stay_studio = 76 * num_stays
    cost_stay_apartment = 77 * num_stays

if num_stays > 14:
    cost_stay_apartment *= 0.90

print(f"Apartment: {cost_stay_apartment:.2f} lv.")
print(f"Studio: {cost_stay_studio:.2f} lv.")

