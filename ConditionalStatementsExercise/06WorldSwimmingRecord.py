import math
from math import floor

record_time = float(input())
distance = float(input())
time = float(input())

slowdown = math.floor(distance / 15) * 12.5
total_time = distance * time + slowdown

if total_time < record_time:
    print("Yes, he succeeded! The new world record is {:.2f} "
          "seconds.".format(total_time))

else:
    print("No, he failed! He was {:.2f} seconds slower."
          .format(total_time - record_time))