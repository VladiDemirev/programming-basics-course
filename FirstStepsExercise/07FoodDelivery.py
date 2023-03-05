CHICKEN = 10.35
FISH = 12.40
VEGGIE = 8.15
DELIVERY = 2.50

num_chicken = int(input())
num_fish = int(input())
num_veggie = int(input())

desert = (CHICKEN * num_chicken + FISH * num_fish + VEGGIE * num_veggie) \
         * 20 / 100

order_price = CHICKEN * num_chicken + FISH * num_fish + VEGGIE * num_veggie \
              + DELIVERY + desert

print("{0:.2f}".format(order_price))