age_Lili = int(input())
price_washing_machine = float(input())
price_single_toy = int(input())

money_received = 0
money_received_toys = 0
num_toys = 0
money_taken_brother = 0
num_even_birthday = 0
# total_money_received = 0

for age_Lili in range(1, age_Lili + 1):
    if age_Lili % 2 != 0:
        num_toys += 1
        money_received_toys = num_toys * price_single_toy
    if age_Lili % 2 == 0:
        num_even_birthday += 1
        money_taken_brother += 1
        money_received += num_even_birthday * 10

total_money_received = money_received_toys + (money_received - money_taken_brother)

if total_money_received >= price_washing_machine:
    print(f"Yes! {abs(total_money_received - price_washing_machine):.2f}")
else:
    print(f"No! {abs(total_money_received - price_washing_machine):.2f}")




