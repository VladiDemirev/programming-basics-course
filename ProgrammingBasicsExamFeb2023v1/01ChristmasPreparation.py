paper_count = int(input())
textile_count = int(input())
glue_count = float(input())
discount = int(input())

total_cost = (paper_count * 5.80) + (textile_count * 7.20) \
                 + (glue_count * 1.20)

discount_cost = total_cost - (total_cost * (discount / 100))

print(f"{discount_cost:.3f}")