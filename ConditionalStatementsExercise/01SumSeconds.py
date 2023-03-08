import math
from math import floor

time1 = int(input())
time2 = int(input())
time3 = int(input())

finish = time1 + time2 + time3
total_time_seconds = finish // 60
seconds = finish % 60
total_time_seconds = math.floor(total_time_seconds)

if finish < 60:
    print(f"0:{finish}")

else:
    if seconds < 10:
        print(f"{total_time_seconds}:0{seconds}")
    else:
        print(f"{total_time_seconds}:{seconds}")