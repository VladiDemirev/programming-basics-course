time_filming = int(input())
num_scenes = int(input())
duration_scene = int(input())

preparation = time_filming * 0.15

total_time = num_scenes * duration_scene + preparation

if total_time <= time_filming:
    print(f"You managed to finish the movie on time! "
          f"You have {round(time_filming - total_time)} minutes left!")
else:
    print(f"Time is up! To complete the movie you need"
          f" {round(total_time - time_filming)} minutes.")