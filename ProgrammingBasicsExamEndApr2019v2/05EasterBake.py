from math import ceil
from sys import maxsize

cakes_count = int(input())

sugar_packet = 0
flour_packet = 0
total_sugar = 0
total_flour = 0
max_sugar = 0
max_flour = 0

for _ in range(cakes_count):
    sugar_spent = int(input())
    total_sugar += sugar_spent

    if sugar_spent > max_sugar:
        max_sugar = sugar_spent

    flour_spent = int(input())
    total_flour += flour_spent

    if flour_spent > max_flour:
        max_flour = flour_spent

sugar_packet = ceil(total_sugar / 950)
flour_packet = ceil(total_flour / 750)

print(f"Sugar: {sugar_packet}")
print(f"Flour: {flour_packet}")
print(f"Max used flour is {max_flour} grams, max used sugar is {max_sugar} grams.")


