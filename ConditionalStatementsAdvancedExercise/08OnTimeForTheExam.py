hour_exam = int(input())
minute_exam = int(input())

hour_arrival = int(input())
minute_arrival = int(input())

exam_time_minutes = hour_exam * 60 + minute_exam
arrival_time_minutes = hour_arrival * 60 + minute_arrival

condition = ""
arrival = ""

if arrival_time_minutes > exam_time_minutes:
    condition = "Late"
elif exam_time_minutes == arrival_time_minutes or exam_time_minutes \
        - arrival_time_minutes <= 30:
    condition = "On time"
elif exam_time_minutes - arrival_time_minutes > 30:
    condition = "Early"

if exam_time_minutes > arrival_time_minutes and exam_time_minutes - arrival_time_minutes < 60:
    arrival = f"{exam_time_minutes - arrival_time_minutes} minutes before the start"
elif exam_time_minutes > arrival_time_minutes and exam_time_minutes - arrival_time_minutes >= 60:
    arrival = f"{(exam_time_minutes - arrival_time_minutes) // 60}:" \
              f"{(exam_time_minutes - arrival_time_minutes) % 60:02d} " \
              f"hours before the start"
elif arrival_time_minutes > exam_time_minutes and arrival_time_minutes - exam_time_minutes < 60:
    arrival = f"{arrival_time_minutes - exam_time_minutes} minutes after the start"
elif arrival_time_minutes > exam_time_minutes and arrival_time_minutes - exam_time_minutes >= 60:
    arrival = f"{(arrival_time_minutes - exam_time_minutes) // 60}:" \
              f"{(arrival_time_minutes - exam_time_minutes) % 60:02d} " \
              f"hours after the start"

print(condition)
print(arrival)

# condition = None
#
# if (hour_exam < hour_arrival) or (hour_exam == hour_arrival and
#                                   minute_arrival > minute_exam):
#     condition = "Late"
# elif (hour_exam == hour_exam and minute_exam == minute_arrival) or \
#         (hour_exam <= hour_arrival and minute_exam - minute_arrival <= 30):
#     condition = "On time"
# elif hour_exam <= hour_arrival and (minute_exam - minute_arrival > 30):
#     condition = "Early"
#
# if hour_arrival - hour_exam >= 1:

