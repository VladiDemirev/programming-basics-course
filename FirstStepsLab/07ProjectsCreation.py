name = input()
projects = int(input())

TIME = 3

hours_needed = projects * TIME

if projects in range(101):
    print(f"The architect {name} will need {hours_needed} hours to complete {projects} project/s. ")
