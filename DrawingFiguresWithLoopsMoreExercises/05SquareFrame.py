user_input = int(input())

for i in range(user_input):
    if i == 0 or i == (user_input - 1):
        print("+ " + "- " * (user_input - 2) + "+")
    else:
        print("| " + "- " * (user_input - 2) + "|")

'''ends = "+"
middle = "-"
sides = "|"'''

'''print(f"{ends} {middle * (user_input - 2)} {ends}")
  else:
    print(f"{sides} {middle * (user_input - 2)} {sides}")'''
