num_pages = int(input())
hour_pages = int(input())
num_days = int(input())

total_days = (num_pages // hour_pages) // num_days

print(total_days)