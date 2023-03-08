VIDEO_CARD = 250

budget = float(input())
num_video_card = int(input())
num_processor = int(input())
num_ram_memory = int(input())

processor = (VIDEO_CARD * num_video_card) * 35 / 100
ram_memory = (VIDEO_CARD * num_video_card) * 10 / 100

total_cost = VIDEO_CARD * num_video_card + processor * num_processor + \
             ram_memory * num_ram_memory

if num_video_card > num_processor:
    total_cost = total_cost - (total_cost * 15 / 100)

if total_cost <= budget:
    print("You have {:.2f} leva left!".format(budget - total_cost))

else:
    print("Not enough money! You need {:.2f} leva more!"
          .format(total_cost - budget))