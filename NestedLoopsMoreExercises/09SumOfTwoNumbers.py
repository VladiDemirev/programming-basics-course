start = int(input())
end = int(input())
magic_number = int(input())

combinations_count = 0

for i in range(start, end + 1):
    for j in range(start, end + 1):
        combinations_count += 1
        if (i + j) == magic_number:
            print(f"Combination N:{combinations_count} ({i} + {j} = {magic_number})")
            exit()
else:
    print(f"{combinations_count} combinations - neither equals {magic_number}")