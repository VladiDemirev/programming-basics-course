desired_height = int(input())
starting_height = desired_height - 30

failed_attempts = 0
jumps_count = 0
is_reached = False

while failed_attempts < 3:
    jump_height = int(input())
    jumps_count += 1

    if starting_height == desired_height:
        if jump_height > starting_height:
            is_reached = True
            break

    if jump_height > starting_height:
        starting_height += 5
        failed_attempts = 0
        continue
    else:
        failed_attempts += 1

if not is_reached:
    print(f"Tihomir failed at {starting_height}cm after {jumps_count} jumps.")
else:
    print(f"Tihomir succeeded, he jumped over {starting_height}cm after {jumps_count} jumps.")
