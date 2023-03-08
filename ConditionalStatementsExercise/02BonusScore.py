first_score = int(input())

bonus = 0

if first_score <= 100:
    bonus = 5

elif 100 < first_score <= 1000:
    bonus = first_score * 20 / 100

else:
    bonus = first_score * 10 / 100

if first_score % 2 == 0:
    bonus += 1

elif first_score % 10 == 5:
    bonus += 2

print(bonus)
print(first_score + bonus)