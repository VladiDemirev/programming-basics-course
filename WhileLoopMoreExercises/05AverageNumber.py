n = int(input())
sum = 0

for _ in range(n):
  number = int(input())
  sum += number

print(f"{sum / n:.2f}")