bitcoins = int(input())
yuans = float(input())
commission = float(input())

eur_bit = (bitcoins * 1168) / 1.95
eur_yuan = (yuans * 0.15 * 1.76) / 1.95

total_eur = (eur_bit + eur_yuan) - ((eur_bit + eur_yuan) * commission / 100)

print(f"{total_eur:.2f}")

