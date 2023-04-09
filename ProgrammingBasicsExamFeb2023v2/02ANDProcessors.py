from math import floor

count_processor = int(input())
count_employees = int(input())
working_days = int(input())

hours_worked = count_employees * working_days * 8
processors_made = floor(hours_worked / 3)

if processors_made >= count_processor:
    print(f"Profit: -> {(processors_made - count_processor) * 110.10:.2f} BGN")
else:
    print(f"Losses: -> {(count_processor - processors_made) * 110.10:.2f} BGN")