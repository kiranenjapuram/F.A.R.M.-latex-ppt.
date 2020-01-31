"""
Project Name: Farming with Autonomous Robotic system usning Machine   
Author List: shreya jagtap 
Filename: waterpump.py
Functions: none
Global Variables: None

"""

import os
import RPi.GPIO as GPIO
import time


##when we set timing in crontab this loop will run at scheduled time.
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(12,GPIO.OUT)
for x in range(2): #loop
 GPIO.output(12,True)
 print("onn")
 time.sleep(2)
 GPIO.output(12,False)
 print("off")
 time.sleep(5)
 os.mkdir(str(int(time.time())))
