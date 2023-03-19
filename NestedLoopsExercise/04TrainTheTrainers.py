n_jury = int(input())

sum_grades = 0
sum_all_grades = 0
num_grades = 0
num_all_grades = 0
num_presentations = 0

is_finished = False

while True:
    presentation_name = input()

    if presentation_name == "Finish":
        print(f"Student's final assessment is {sum_all_grades / num_all_grades:.2f}.")
        break

    num_presentations += 1

    for i in range(1, n_jury + 1):
        grade = float(input())
        sum_grades += grade
        sum_all_grades += grade
        num_grades += 1
        num_all_grades += 1

    print(f"{presentation_name} - {sum_grades / num_grades:.2f}.")
    sum_grades = 0
    num_grades = 0
