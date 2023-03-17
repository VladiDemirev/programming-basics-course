period = int(input())

treated_patients = 0
untreated_patients = 0

doctors = 7

for i in range(1, period+1):
    if i % 3 == 0:
        if untreated_patients > treated_patients:
            doctors += 1
    patients_per_day = int(input())
    if patients_per_day <= doctors:
        treated_patients += patients_per_day
    else:
        treated_patients += doctors
        untreated_patients += (patients_per_day - doctors)

print(f"Treated patients: {treated_patients}.")
print(f"Untreated patients: {untreated_patients}.")
