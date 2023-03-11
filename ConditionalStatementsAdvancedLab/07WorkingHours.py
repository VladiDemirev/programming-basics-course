hour = int(input())
day = input()
working_day = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday",
            "Saturday"]
if 10 <= hour <= 18 and day in working_day:
    print("open")
else:
    print("closed")