last_sector = input()
rows_first_sector = int(input())
seats_odd_row = int(input())
seats_even_row = seats_odd_row + 2
number_seats = 0
total_seats = 0

for sector in range(ord("A"), ord(last_sector.upper()) + 1):
    for row in range(1, rows_first_sector + 1):
        if row % 2 != 0:
            number_seats = seats_odd_row
        else:
            number_seats = seats_even_row
        for seats in range(ord("a"), ord("a") + number_seats):
            print(f"{chr(sector)}{row}{chr(seats)}")
            total_seats += 1

    rows_first_sector += 1

print(total_seats)