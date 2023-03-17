num_cargoes = int(input())

avg_price_ton = 0
bus_tonnage = 0
truck_tonnage = 0
train_tonnage = 0

total_cargo_tonnage = 0

for i in range(0, num_cargoes):
    cargo_tonnage = int(input())
    if cargo_tonnage <= 3:
        bus_tonnage += cargo_tonnage
    elif 4 <= cargo_tonnage <= 11:
        truck_tonnage += cargo_tonnage
    else:
        train_tonnage += cargo_tonnage
    total_cargo_tonnage += cargo_tonnage

print(f"{(bus_tonnage * 200 + truck_tonnage * 175 + train_tonnage * 120) / total_cargo_tonnage:.2f}")
print(f"{bus_tonnage / total_cargo_tonnage *100:.2f}%")
print(f"{truck_tonnage / total_cargo_tonnage *100:.2f}%")
print(f"{train_tonnage / total_cargo_tonnage *100:.2f}%")