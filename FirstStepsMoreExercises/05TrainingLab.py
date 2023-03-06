import math

lab_w, lab_h = float(input()), float(input())

lab_h = lab_h - 1

WORKING_PLACE_w = 1.2
WORKING_PLACE_h = 0.7

num_working_places_h = lab_h // WORKING_PLACE_h
num_working_places_w = lab_w // WORKING_PLACE_w

total_num_working_places = num_working_places_w * num_working_places_h - 3

print(math.floor(total_num_working_places))
