bottles_count = int(input()) * 750
loading = 0
clean_plates = 0
clean_pots = 0

while bottles_count >= 0:
    dirty_dishes = input()
    loading += 1

    if dirty_dishes == "End":
        print("Detergent was enough!")
        print(f"{clean_plates} dishes and {clean_pots} pots were washed.")
        print(f"Leftover detergent {bottles_count} ml.")
        break
    else:
        dirty_dishes = int(dirty_dishes)

    if loading % 3 == 0:
        clean_pots += dirty_dishes
        bottles_count -= (dirty_dishes * 15)
    else:
        clean_plates += dirty_dishes
        bottles_count -= (dirty_dishes * 5)

else:
    print(f"Not enough detergent, {abs(bottles_count)} ml. more necessary!")