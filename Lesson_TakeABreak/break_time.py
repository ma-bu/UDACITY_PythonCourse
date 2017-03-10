#!/usr/bin/python3

# import necessary modules
import time
import webbrowser


# set break count how often a break reminder supposed to appear
totalBreaks = 3

# set waiting time between the reminders
sleepTime = 1*10  # minutes*seconds

# set url of the break video
clipUrl = 'https://www.youtube.com/watch?v=a1Y73sPHKxw'


# initial counter for the break loop
breakCount = 0

# tell the user the program has been started and also show the current time as start point
print('The program break_time has been started at: ' + time.ctime())

while (breakCount < totalBreaks):

    # set timer --> wait for the defined time
    time.sleep(sleepTime)

    # open a webbrowser with the given URL
    webbrowser.open(clipUrl)

    breakCount = breakCount + 1

    print('Reminder ' + str(breakCount) + ' started at: ' + time.ctime())

# print finish message
print('Successful finished the program break_time and created ' + str(totalBreaks) + ' reminders each waiting for ' + str(sleepTime) + ' seconds')
