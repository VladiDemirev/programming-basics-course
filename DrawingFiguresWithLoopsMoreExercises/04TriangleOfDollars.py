user_input = int(input())

for row in range(1, user_input + 1):
    for col in range(1, row + 1):
      if row == col:
        print("$")
      else:
        print("$", end=" ")