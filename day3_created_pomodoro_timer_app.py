# Pomodoro-timer : The pomodoro-timer technique is used for time-management where you break your work into
# shorter interval, traditionally, 25 minutes of work and 5 minute break time. This is called 1 cycle of pomodoro.
# After 4 such cycles(1 round of pomodoro) you take 15-minute break.


from datetime import datetime
from datetime import timedelta
import time
import subprocess

pomodoro_cycles = 0


# function to run the timer
def run_pomodoro_timer():
    current_time, future_time, finish_time = get_time()
    global pomodoro_cycles
    sound = 0
    while True:
        if current_time < future_time:  # this statement checks for task time
            print(f"It's working time:{datetime.strftime(current_time,'%Y-%m-%d %H:%M:%S')}")
        elif future_time <= current_time < finish_time:  # this is for break time
            sound = sound + 1
            if sound == 1:  # play the beep sound when it is break time
                subprocess.call(["afplay","dit.wav"])
                print(f"Break-time :{datetime.strftime(current_time,'%Y-%m-%d %H:%M:%S')}")
            else:
                print(f"Break-time :{datetime.strftime(current_time, '%Y-%m-%d %H:%M:%S')}")
        else:  # checks if current time passed the break time
            pomodoro_cycles = pomodoro_cycles + 1
            print(f"Good job!you have completed {pomodoro_cycles} cycle of Pomodoro-timer :{datetime.strftime(current_time,'%Y-%m-%d %H:%M:%S')}")
            break
        time.sleep(20)  # sleep for few seconds and calculate current time again to check the loop
        current_time = datetime.now()
    get_user_response(pomodoro_cycles)


#  function to get the user response
def get_user_response(cycle_counter):  # Get the user response before each cycle
    user_response = input("Do you want to start the next 25 minute cycle : Press (y or n) and enter: ")
    if str.lower(user_response) == 'y':
        if cycle_counter < 4:  # check for pomodoro round
            run_pomodoro_timer()
        elif cycle_counter >= 4:
            print("You have completed 1 round (4 cycles) of pomodoro timer. You can take 15 min break.")
    else:
        print(f"You have completed total {cycle_counter} cycles of pomodoro-timer.")


# function to get the timer values
def get_time():
    time_now = datetime.now()  # current time
    time_pomodoro = 25 * 60     # convert pomodoro time 25 min to seconds
    time_pomodoro_break = 5 * 60    # convert break time of 5min into seconds
    time_future = time_now + timedelta(seconds=time_pomodoro)  # calculate the time after 25 minutes
    time_finish = time_future + timedelta(seconds=time_pomodoro_break)  # calculating the final pomodoro finish time
    return time_now, time_future, time_finish


# main program
if __name__ == '__main__':
    run_pomodoro_timer()  # call the timer function
