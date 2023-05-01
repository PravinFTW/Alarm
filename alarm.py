import datetime
import time
import playsound

# Function to play alarm sound
def play_sound(sound_file):
    playsound.playsound(sound_file)

# Function to set the alarm
def set_alarm(alarm_time, sound_file):
    while True:
        current_time = datetime.datetime.now()
        formatted_current_time = current_time.strftime("%H:%M:%S")
        if formatted_current_time == alarm_time:
            print("Time to wake up!")
            play_sound(sound_file)
            break
        time.sleep(1)

# Get alarm time from user
alarm_time = input("Enter the time to set the alarm (in format HH:MM:SS): ")
sound_file ="alarm.mp3"

# Call set_alarm function to start the alarm
set_alarm(alarm_time, sound_file)
