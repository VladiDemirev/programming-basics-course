visitors = int(input())

back = 0
chest = 0
legs = 0
abs = 0
shake = 0
bar = 0
work_out = 0
supplement = 0
total = 0

for _ in range(visitors):
    activity = input()

    if activity == "Back":
        back += 1
    elif activity == "Chest":
        chest += 1
    elif activity == "Legs":
        legs += 1
    elif activity == "Abs":
        abs += 1
    elif activity == "Protein shake":
        shake += 1
    else:
        bar += 1

    work_out = back + chest + legs + abs
    supplement = shake + bar
    total = work_out + supplement

print(f"{back} - back")
print(f"{chest} - chest")
print(f"{legs} - legs")
print(f"{abs} - abs")
print(f"{shake} - protein shake")
print(f"{bar} - protein bar")
print(f"{work_out / total * 100:.2f}% - work out")
print(f"{supplement / total * 100:.2f}% - protein")