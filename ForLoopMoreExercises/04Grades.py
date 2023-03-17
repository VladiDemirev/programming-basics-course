num_students = int(input())

excellent_students = 0
good_students = 0
average_students = 0
failed_students = 0

sum_grades = 0

for i in range(1, num_students+1):
    exam_grade = float(input())
    if exam_grade >= 5.00:
        excellent_students += 1
    elif 4.00 <= exam_grade <= 4.99:
        good_students += 1
    elif 3.00 <= exam_grade <= 3.99:
        average_students += 1
    else:
        failed_students += 1
    sum_grades += exam_grade

print(f"Top students: {excellent_students / num_students * 100:.2f}%")
print(f"Between 4.00 and 4.99: {good_students / num_students * 100:.2f}%")
print(f"Between 3.00 and 3.99: {average_students / num_students * 100:.2f}%")
print(f"Fail: {failed_students / num_students * 100:.2f}%")
print(f"Average: {sum_grades / num_students:.2f}")
