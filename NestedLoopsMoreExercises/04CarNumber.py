interval_beg = int(input())
interval_end = int(input())

car_plate = []

for i in range(interval_beg, interval_end + 1):
  for j in range(interval_beg, interval_end + 1):
    for k in range(interval_beg, interval_end + 1):
      for l in range(interval_beg, interval_end + 1):
        if (i % 2 == 0 and l % 2 == 0) or (i % 2 != 0 and l % 2 != 0):
          continue
        elif i <= l:
          continue
        elif (j + k) % 2 != 0:
          continue
        else:
          car_plate.extend([i, j, k, l])
          print(*car_plate, sep="", end=" ")
          car_plate.clear()