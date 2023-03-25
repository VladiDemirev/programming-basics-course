movie = input()
hall = input()
tickets = int(input())

if movie == "A Star Is Born":
    if hall == "normal":
        cost = 7.50
    elif hall == "luxury":
        cost = 10.50
    else:
        cost = 13.50

elif movie == "Bohemian Rhapsody":
    if hall == "normal":
        cost = 7.35
    elif hall == "luxury":
        cost = 9.45
    else:
        cost = 12.75

elif movie == "Green Book":
    if hall == "normal":
        cost = 8.15
    elif hall == "luxury":
        cost = 10.25
    else:
        cost = 13.25

else:
    if hall == "normal":
        cost = 8.75
    elif hall == "luxury":
        cost = 11.55
    else:
        cost = 13.95

total_cost = cost * tickets

print(f"{movie} -> {total_cost:.2f} lv.")









