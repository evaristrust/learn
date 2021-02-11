import time
import os

from pynotifier import Notification


Notification(
	title='BIRTHDAY NOTIFICATIONS',
	description='We remind you of your friends having BD today!',
    # icon_path= 'path/to/image/file/icon.ico', # ico for windows or png for linux
	duration=5,                              # Duration in seconds
	urgency=Notification.URGENCY_CRITICAL
).send()

# creating a program that will notify me to wish BD to my friends

# 1. open the bd file to store BD info

with open('bd.txt', 'w') as bd_file:
    print('STORE THE INFO HERE: FORMAT: MONTHDAY FIRSTNAME LASTNAME', file=bd_file)

def get_bd_notifications():
    file_name = open('bd.txt', 'r')
    flag = 0
    today = time.strftime('%m%d')

    for line in file_name:
        if today in line:
            line = line.split(' ')
            flag = 1
            # line[0] is date, line[1] is FirstName, line[2] is lastName
            os.system('notify-send "Birthdays Today: ' + line[1]
                      + ' ' + line[2] + '"')
    if flag == 0:
        os.system('notify-send "No Birthdays Today!"')

if __name__ == '__main__':
    get_bd_notifications()