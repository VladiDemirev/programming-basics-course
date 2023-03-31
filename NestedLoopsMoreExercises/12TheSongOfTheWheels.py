control_num = int(input())
combinations = 0
password = None
is_found = False

for a in range(1, 10):
    for b in range(1, 10):
        for c in range(1, 10):
            for d in range(1, 10):
                if (
                        ((a * b + c * d) == control_num) and
                        (a < b) and
                        (c > d)
                ):
                    combinations += 1
                    print(f"{a}{b}{c}{d}", end=" ")

                    if combinations == 4:
                        is_found = True
                        password = f"{a}{b}{c}{d}"

if is_found:
    print(f"\nPassword: {password}")
else:
    print("\nNo!")
