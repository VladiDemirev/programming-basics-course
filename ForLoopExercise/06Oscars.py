actor_name = input()
academy_points = float(input())
num_jury = int(input())

points_actor = academy_points

for i in range(0, num_jury):
    name_jury = input()
    jury_points = float(input())
    points_actor += (len(name_jury) * jury_points) / 2
    if points_actor > 1250.5:
        print(f"Congratulations, {actor_name} got a nominee for leading "
              f"role with {points_actor:.1f}!")
        break

if points_actor <= 1250.5:
    print(f"Sorry, {actor_name} you need {1250.5 - points_actor:.1f} more!")
