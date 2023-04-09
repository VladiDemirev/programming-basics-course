from math import floor

cat_breed = input()
cat_gender = input()

cat_months = 0
longevity = 0
is_valid = True

if cat_breed == "British Shorthair":
    if cat_gender == "m":
        longevity = 13
    else:
        longevity = 14
elif cat_breed == "Siamese":
    if cat_gender == "m":
        longevity = 15
    else:
        longevity = 16
elif cat_breed == "Persian":
    if cat_gender == "m":
        longevity = 14
    else:
        longevity = 15
elif cat_breed == "Ragdoll":
    if cat_gender == "m":
        longevity = 16
    else:
        longevity = 17
elif cat_breed == "American Shorthair":
    if cat_gender == "m":
        longevity = 12
    else:
        longevity = 13
elif cat_breed == "Siberian":
    if cat_gender == "m":
        longevity = 11
    else:
        longevity = 12
else:
    is_valid = False

cat_months = longevity * 12 / 6

if is_valid:
    print(f"{floor(cat_months)} cat months")
else:
    print(f"{cat_breed} is invalid cat!")