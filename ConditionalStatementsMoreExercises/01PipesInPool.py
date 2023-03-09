# User inputs
pool_volume_V = int(input())
pipe1_flow_rate_hour = int(input())
pipe2_flow_rate_hour = int(input())
absent_hours_H = float(input())

# Water from pipes 1&2 and total water in the pool when the worker returns
pipe1_water_flown = pipe1_flow_rate_hour * absent_hours_H
pipe2_water_flown = pipe2_flow_rate_hour * absent_hours_H
total_water_flown = pipe1_water_flown + pipe2_water_flown

# Conditions
if pool_volume_V >= total_water_flown:
    print(f"The pool is {((total_water_flown / pool_volume_V) * 100):.2f}% full. "
          f"Pipe 1: {((pipe1_water_flown / total_water_flown) * 100):.2f}%. "
          f"Pipe 2: {((pipe2_water_flown / total_water_flown) * 100):.2f}%.")
else:
    print(f"For {absent_hours_H:.2f} hours the pool overflows with "
          f"{(total_water_flown - pool_volume_V):.2f} liters.")



