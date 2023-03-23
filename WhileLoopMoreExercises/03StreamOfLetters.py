c_counter = 0
o_counter = 0
n_counter = 0

letters = []

while True:
    user_input = input()

    if user_input.isalpha() == False:
        continue

    if user_input not in ("con"):
        letters.append(user_input)

    elif user_input == "c":
        c_counter += 1
        if c_counter > 1:
            letters.append(user_input)

    elif user_input == "o":
        o_counter += 1
        if o_counter > 1:
            letters.append(user_input)

    elif user_input == "n":
        n_counter += 1
        if n_counter > 1:
            letters.append(user_input)

    if c_counter >= 1 and o_counter >= 1 and n_counter >= 1:
        print(''.join(letters), end=" ")
        letters.clear()

        c_counter = 0
        o_counter = 0
        n_counter = 0

    if user_input == "End":
        break 