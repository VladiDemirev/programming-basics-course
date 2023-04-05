trunk_capacity = float(input())

loaded_baggage = 0

while trunk_capacity > 0:
    suitcase_volume = input()

    if suitcase_volume == "End":
        print("Congratulations! All suitcases are loaded!")
        break
    else:
        suitcase_volume = float(suitcase_volume)

    loaded_baggage += 1

    if loaded_baggage % 3 == 0:
        suitcase_volume *= 1.1

    if suitcase_volume > trunk_capacity:
        print("No more space!")
        loaded_baggage -= 1
        break
    else:
        trunk_capacity -= suitcase_volume


print(f"Statistic: {loaded_baggage} suitcases loaded.")