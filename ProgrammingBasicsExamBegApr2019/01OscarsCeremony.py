rent = int(input())

figures = rent * 0.70
catering = figures * 0.85
sound = catering * 0.50

cost = rent + figures + catering + sound

print(f"{cost:.2f}")