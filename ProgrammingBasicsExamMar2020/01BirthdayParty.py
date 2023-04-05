hall_rent = float(input())

cake = hall_rent * 0.2
drinks = cake * 0.55
animator = hall_rent / 3

budget = hall_rent + cake + drinks + animator

print(f"{budget:.1f}")
