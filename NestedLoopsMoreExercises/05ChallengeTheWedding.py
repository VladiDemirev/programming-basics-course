male_clients = int(input())
female_clients = int(input())
max_tables = int(input())

for i in range(1, male_clients + 1):
  for j in range(1, female_clients + 1):
    max_tables -= 1

    if max_tables < 0:
      break

    print(f"({i} <-> {j})", end=" ") 