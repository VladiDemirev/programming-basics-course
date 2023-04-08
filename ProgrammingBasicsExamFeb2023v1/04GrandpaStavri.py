days_count = int(input())

liters_count = 0
total_degrees = 0

for _ in range(days_count):
    schnapps_quantity = float(input())
    liters_count += schnapps_quantity

    schnapps_degrees = float(input())
    current_degrees = schnapps_quantity * schnapps_degrees
    total_degrees += current_degrees

degrees_all_schnapps = total_degrees / liters_count

print(f"Liter: {liters_count:.2f}")
print(f"Degrees: {degrees_all_schnapps:.2f}")

if degrees_all_schnapps < 38:
    print("Not good, you should baking!")
elif 38 <= degrees_all_schnapps <= 42:
    print("Super!")
elif degrees_all_schnapps > 42:
    print("Dilution with distilled water!")


