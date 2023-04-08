time = 1
meters_to_climb = 8848 - 5364
total_meters = 0

while time <= 5:
    user_input = input()

    if user_input == "END":
        break
    elif user_input == "Yes":
        time += 1

    meters_climbed = int(input())
    total_meters += meters_climbed

    if total_meters >= meters_to_climb:
        print(f"Goal reached for {time} days!")
        break

if user_input == "END":
    print("Failed!")
    print(f"{total_meters + 5364}")
elif time > 5:
    print("Failed!")
    print(f"{total_meters + 5364 - meters_climbed}")


