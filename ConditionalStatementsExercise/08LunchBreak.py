import math
from math import ceil

series_name = input()
episode_duration = int(input())
break_duration = int(input())

lunch_time = (1 / 8) * break_duration
rest_time = (1 / 4) * break_duration

watching_time = break_duration - (lunch_time + rest_time)
time_needed = episode_duration - watching_time

if watching_time >= episode_duration:
    print("You have enough time to watch {} and left with {} minutes free time."
          .format(series_name, math.ceil(watching_time - episode_duration)))

else:
    print("You don't have enough time to watch {}, you need {} more minutes."
          .format(series_name, math.ceil(episode_duration - watching_time)))
