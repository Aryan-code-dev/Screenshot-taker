import schedule
import time
import pyautogui
import cv2
import numpy as np
frequency = int(input("Enter the duration between every screenshot (IN SECONDS)"))
duration = int(input("Enter the time period in minutes  for which the program should run"))
file_location = str(input("Enter the folder location in which the "))
time_input = str(input("Enter the time at which program should start in HH:MM format"))
duration = duration*60
loop = duration/frequency


def job():

    i = 0
    while i != loop:
        myScreenshot = pyautogui.screenshot()
        myScreenshot = cv2.cvtColor(np.array(myScreenshot), cv2.COLOR_RGB2BGR)
        cv2.imwrite(file_location+"\ " + str(i)+".png", myScreenshot)
        i += 1
        time.sleep(frequency)


schedule.every().day.at(time_input).do(job)

while True:
    schedule.run_pending()


