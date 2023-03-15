num_open_tabs = int(input())
salary = float(input())

FINE_FB = 150
FINE_IG = 100
FINE_RD = 50

deduction = 0

for i in range(0, num_open_tabs):
    website_name = input()
    if website_name == "Facebook":
        salary = salary - FINE_FB
    elif website_name == "Instagram":
        salary = salary - FINE_IG
    elif website_name == "Reddit":
        salary = salary - FINE_RD
    if salary <= 0:
        print("You have lost your salary.")
        break

if salary > 0:
    print(f"{salary:.0f}")


