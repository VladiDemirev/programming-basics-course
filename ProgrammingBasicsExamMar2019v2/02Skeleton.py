minutes = int(input())
seconds = int(input())
length = float(input())
time_100_meters = int(input())

test_time = minutes * 60 + seconds

acceleration = length / 120 * 2.5
competitor_time = length / 100 * time_100_meters - acceleration

if competitor_time <= test_time:
    print(f"Marin Bangiev won an Olympic quota!\nHis time is {competitor_time:.3f}.")
else:
    print(f"No, Marin failed! He was {competitor_time - test_time:.3f} second slower.")
