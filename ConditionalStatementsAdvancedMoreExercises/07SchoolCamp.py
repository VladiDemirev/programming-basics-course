season = input()            # Winter, Spring or Summer
group_type = input()        # boys, girls or mixed
num_students = int(input())
num_overnight_stay = int(input())

cost_overnight_stay = 0
discount = 0
sport_type = ""

if season == "Winter":
    if group_type == "boys":
        cost_overnight_stay = 9.60
        sport_type = "Judo"
    elif group_type == "girls":
        cost_overnight_stay = 9.60
        sport_type = "Gymnastics"
    elif group_type == "mixed":
        cost_overnight_stay = 10
        sport_type = "Ski"

elif season == "Spring":
    if group_type == "boys":
        cost_overnight_stay = 7.20
        sport_type = "Tennis"
    elif group_type == "girls":
        cost_overnight_stay = 7.20
        sport_type = "Athletics"
    elif group_type == "mixed":
        cost_overnight_stay = 9.50
        sport_type = "Cycling"

elif season == "Summer":
    if group_type == "boys":
        cost_overnight_stay = 15
        sport_type = "Football"
    elif group_type == "girls":
        cost_overnight_stay = 15
        sport_type = "Volleyball"
    elif group_type == "mixed":
        cost_overnight_stay = 20
        sport_type = "Swimming"

gross_cost_overnight_stay = num_students * num_overnight_stay * cost_overnight_stay

if num_students >= 50:
    discount = gross_cost_overnight_stay * 0.5
elif 20 <= num_students < 50:
    discount = gross_cost_overnight_stay * 0.15
elif 10 <= num_students < 20:
    discount = gross_cost_overnight_stay * 0.05

net_cost_overnight_stay = gross_cost_overnight_stay - discount

print(f"{sport_type} {net_cost_overnight_stay:.2f} lv.")
