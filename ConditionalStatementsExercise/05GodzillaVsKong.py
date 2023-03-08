budget = float(input())
support_actor = int(input())
clothes = float(input())

background = budget * 10 / 100

if support_actor > 150:
    expenses = (support_actor * clothes) - \
               (support_actor * clothes) * 10 / 100 + background

else:
    expenses = support_actor * clothes + background

if expenses > budget:
    print("Not enough money!")
    print("Wingard needs {:.2f} leva more.".format(expenses - budget))

else:
    print("Action!")
    print("Wingard starts filming with {:.2f} leva left."
          .format(budget - expenses))