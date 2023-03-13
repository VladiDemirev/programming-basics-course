number = float(input())

number1 = 0

while number >= 0:
    number1 = number * 2
    print(f"Result: {number1:.2f}")
    number = float(input())
if number < 0:
    print("Negative number!")
