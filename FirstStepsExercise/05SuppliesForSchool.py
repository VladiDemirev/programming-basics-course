PRICE_PENS = 5.80
PRICE_MARKERS = 7.20
PRICE_CLEANER = 1.20

pens = int(input())
markers = int(input())
cleaner = int(input())
discount = int(input())

discount_amount = ((pens * PRICE_PENS + markers * PRICE_MARKERS + cleaner
                    * PRICE_CLEANER) * (discount / 100))
money = (pens * PRICE_PENS + markers * PRICE_MARKERS + cleaner
         * PRICE_CLEANER) - discount_amount

print(money)