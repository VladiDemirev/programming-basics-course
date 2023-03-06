house_height_x = float(input())
wall_length_y = float(input())
roof_height_h = float(input())

# Green paint area calculation

FRONT_WALL_DOOR_W = 1.2
FRONT_WALL_DOOR_H = 2
front_wall_door_area = FRONT_WALL_DOOR_W * FRONT_WALL_DOOR_H

back_wall_area = house_height_x ** 2
front_wall_area = back_wall_area - front_wall_door_area

WINDOW_W = 1.5
window_area = WINDOW_W ** 2

side_wall_area = (house_height_x * wall_length_y) - window_area

area_without_roof = front_wall_area + back_wall_area \
                    + side_wall_area * 2

# Red paint area calculation

rectangle_roof_area = wall_length_y * house_height_x

triangle_roof_area = (house_height_x * roof_height_h) / 2

roof_area = rectangle_roof_area * 2 + triangle_roof_area * 2

# Needed green paint 1l = 3.4 sq.m.
# Needed red paint 1l = 4.3 sq.m.

needed_green_paint = area_without_roof / 3.4
needed_red_paint = roof_area / 4.3

print(f"{needed_green_paint:.2f}")
print(f"{needed_red_paint:.2f}")
