import time

def main():
    count_down_time=int(input("Enter the countdown time interms of second: "))
    # Use input interms of second

    i=count_down_time
    while i>0:
        sec=i%60
        # It is divided by 60 because there are 60sec per min
        min=int(i/60)%60
        # It is divided by 60 because there are 60 min per hr
        hour=int(i/3600)%24
        # It is divided by 24 because there is 24hr per day
        day=int(i/86400)


        print(f"{day:02} day/days:{hour:02} hr:{min:02} min:{sec:02} sec")#pad 0 when to reach the desired number of digit
        
        time.sleep(1)
        # As long as the count_down_time is greater than 0 it is going to sleep 1 second on each loop
        i=i-1
        # Break the loop
    print("TIME'S UP!")
main()