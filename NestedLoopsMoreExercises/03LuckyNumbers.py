number = int(input())

for i in range(1000, 10000):
  i = str(i)
  if str(0) in i:
    continue
  if (number % (int(i[0]) + int(i[1])) == 0) and (int(i[0]) + int(i[1]) == int(i[2]) + int(i[3])):
    print(i, end=" ")