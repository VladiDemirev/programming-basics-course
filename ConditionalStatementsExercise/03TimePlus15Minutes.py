hours = int(input())    #   hours are between 0-23
minutes = int(input())  #   minutes are between 0-59

TIME = 15

if (minutes + TIME) > 60 and hours < 23:
    print(f"{hours+1}:0{(minutes+15) - 60}")

elif (minutes + TIME) > 60 and hours == 23:
    print(f"0:{(minutes + 15) - 60}")

else:
    print(f"{hours}:{minutes+15}")