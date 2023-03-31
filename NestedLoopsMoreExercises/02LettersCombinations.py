letter1 = input()
letter2 = input()
letter3 = input()

counter = 0
combination = []

for i in range(ord(letter1), ord(letter2) + 1):
    for j in range(ord(letter1), ord(letter2) + 1):
        for k in range(ord(letter1), ord(letter2) + 1):
            combination.extend([chr(i), chr(j), chr(k)])
            if len(combination) == 3:
                if letter3 in combination:
                    combination.clear()
                    continue
                else:
                    print("".join(combination), end=" ")
                    counter += 1
                    combination.clear()

print(counter, end="")
