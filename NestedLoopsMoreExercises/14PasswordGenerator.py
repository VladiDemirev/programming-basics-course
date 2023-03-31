num_n = int(input())
num_L = int(input())

for sym1 in range(1, num_n):
  for sym2 in range(1, num_n):
    for sym3 in range(ord("a"), (ord("a") + num_L)):
      for sym4 in range(ord("a"), (ord("a") + num_L)):
        for sym5 in range(1, num_n + 1):
          if (sym5 <= sym1) or (sym5 <= sym2):
            continue
          print(f"{sym1}{sym2}{chr(sym3)}{chr(sym4)}{sym5}", end=" ")