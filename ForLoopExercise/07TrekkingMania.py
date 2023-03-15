num_group = int(input())

num_people_Musala = 0
num_people_Montblanc = 0
num_people_Kilimanjaro = 0
num_people_K2 = 0
num_people_Everest = 0

total_people = 0

for i in range (0, num_group):
    num_people_in_group = int(input())
    total_people += num_people_in_group
    if num_people_in_group <= 5:
        num_people_Musala += num_people_in_group
    elif 6 <= num_people_in_group <= 12:
        num_people_Montblanc += num_people_in_group
    elif 13 <= num_people_in_group <= 25:
        num_people_Kilimanjaro += num_people_in_group
    elif 26 <= num_people_in_group <= 40:
        num_people_K2 += num_people_in_group
    elif num_people_in_group >= 41:
        num_people_Everest += num_people_in_group

print(f"{(num_people_Musala / total_people) * 100:.2f}%")
print(f"{(num_people_Montblanc / total_people) * 100:.2f}%")
print(f"{(num_people_Kilimanjaro / total_people) * 100:.2f}%")
print(f"{(num_people_K2 / total_people) * 100:.2f}%")
print(f"{(num_people_Everest / total_people) * 100:.2f}%")