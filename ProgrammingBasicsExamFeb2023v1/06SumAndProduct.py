n = int(input())
is_found = False

for a in range(1, 10):
    for b in range(9, a - 1, -1):
        for c in range(10):
            for d in range(9, c - 1, -1):
                if ((a + b + c + d) == (a * b * c * d)) and n % 10 == 5:
                    is_found = True
                    print(f"{a}{b}{c}{d}")
                    break
                elif (((a * b * c * d) // (a + b + c + d)) == 3) and (n % 3 == 0):
                    is_found = True
                    print(f"{d}{c}{b}{a}")
                    break

            if is_found:
                break
            else:
                continue

        if is_found:
            break
        else:
            continue

    if is_found:
        break
    else:
        print("Nothing found")
        exit()
