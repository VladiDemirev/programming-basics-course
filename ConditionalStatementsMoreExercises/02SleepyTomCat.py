# User input
rest_days = int(input())

# Constants
PLAY_NORM = 30000
WORK_DAY_PLAYTIME = 63
REST_DAY_PLAYTIME = 127
YEAR_LENGTH = 365

work_days = YEAR_LENGTH - rest_days

yearly_playtime = work_days * WORK_DAY_PLAYTIME + rest_days * REST_DAY_PLAYTIME

# Conditions
if yearly_playtime > PLAY_NORM:
    print("Tom will run away")
    print(f"{(yearly_playtime - PLAY_NORM) // 60} hours and "
          f"{(yearly_playtime - PLAY_NORM) % 60} minutes more for play")
else:
    print("Tom sleeps well")
    print(f"{(PLAY_NORM - yearly_playtime) // 60} hours and "
      f"{(PLAY_NORM - yearly_playtime) % 60} minutes less for play")
