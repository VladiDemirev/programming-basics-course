num_a = int(input())
num_b = int(input())
max_pass = int(input())
num_combinations = 0

for symbol_1 in range(ord("#"), ord("#") + num_a):
    for symbol_2 in range(ord("@"), ord("@") + num_a):
        for symbol_2 in range(ord("@"), ord("@") + num_a):
            for symbol_1 in range(ord("#"), ord("#") + num_a):
                for symbol_3 in range(1, num_a + 1):
                    for symbol_4 in range(1, num_b + 1):
                        num_combinations += 1
                        if num_combinations > max_pass:
                            exit()
                        if num_combinations > num_a * num_b:
                            exit()
                        print(f"{chr(symbol_1)}{chr(symbol_2)}{symbol_3}{symbol_4}{chr(symbol_2)}{chr(symbol_1)}",
                              end="|")
                        symbol_1 += 1
                        symbol_2 += 1
                        if symbol_1 > 55:
                            symbol_1 = 35
                        if symbol_2 > 96:
                            symbol_2 = 64