record = float(input())
distance = float(input())
time = float(input())

slowdown = (distance // 50) * 30

total_time = distance * time + slowdown

if total_time < record:
    print(f"Yes! The new record is {total_time:.2f} seconds.")
else:
    print(f"No! He was {total_time-record:.2f} seconds slower.")