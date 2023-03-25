from sys import maxsize

movies_count = int(input())
max = 0
highest = -maxsize
lowest = maxsize
current_rating = 0
total_rating = 0

for _ in range(movies_count):
    movie = input()
    rating = float(input())
    total_rating += rating

    if rating > highest:
        highest = movie
    elif rating < lowest:
        lowest = movie

print(f"{movie} is with highest rating: {rating}")
print(f"{movie} is with lowest rating: {rating}")
print(f"Average rating: {total_rating / movies_count:.1f}")


