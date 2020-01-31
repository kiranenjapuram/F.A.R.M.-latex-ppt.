#! /usr/bin/env python



"""
Project Name: Farming with Autonomous Robotic system usning Machine   
Author List: Kiran Enjapuram ,Ajinkya Giri , Chinmay Lokare
Filename: go_to_location.py
Functions: walk , callback
Global Variables: None

"""


from time import sleep
import RPi.GPIO as GPIO
import rospy
import numpy
#import os
from std_msgs.msg import Float64
from std_msgs.msg import String

#import subprocess #go to the end of callback function

DIR = 12
STEP =5
CW = 1
CCW = 0
EN=8
#M0=8
#M1=11
#M2=25
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(EN, GPIO.OUT)
#GPIO.setup(M0, GPIO.OUT)
#GPIO.setup(M1, GPIO.OUT)
#GPIO.setup(M2, GPIO.OUT)
GPIO.setup(DIR, GPIO.OUT)
GPIO.setup(STEP, GPIO.OUT)
GPIO.output(EN,GPIO.HIGH)
GPIO.output(DIR,GPIO.HIGH)
delay=0.005
GPIO.output(EN, GPIO.LOW)


"""
Function Name:	walk
Input: none
Output: none
Logic: this will run the subscriber node at topic bot_position.

""" 


def walk():
        rospy.sleep(0.1)
        rospy.init_node('run',anonymous=True)
        rospy.Subscriber('bot_position',Float64,callback)
        rospy.spin()



"""
Function Name: callback
Input: input is given by the publisher node.
Output: the output will give the no of steps for stepper to move.
Logic: the arithmetic operation is stored in variable "angle" if value is positive stepper will run in clockwise else it will  run in anticlockwise.

"""


def callback(current_location):
        rospy.loginfo("current location is %f",current_location.data)
        destination=input("enter the destination=")
        difference=destination-current_location.data
	#rospy.loginfo("starting motor..")
	angle=(1.78*360*difference)/34.54
	#angle=100*difference/7.62
	if angle > 0:                                                ##FOR CLOCKWISE DIRECTION
	        #rospy.loginfo("running motor %f cm forward",difference)
		step_count=(angle)/1.8
		rospy.loginfo(step_count)
		for x in numpy.arange((step_count)):
			GPIO.output(EN, GPIO.LOW)
			GPIO.output(DIR, GPIO.LOW)
			GPIO.output(STEP, GPIO.HIGH)
			sleep(delay)
			GPIO.output(STEP, GPIO.LOW)
			sleep(delay)
			#GPIO.output(EN,GPIO.HIGH)
	 	#sleep(0.005)
		#rospy.loginfo("moving right side towards destination",difference.data)

	elif angle < 0:                                            ##FOR ANTICLOCKWISE DIRECTION
		angle=(angle)*(-1)
		#rospy.loginfo("running motor %f cm BACKWARD",difference)
		step_count=(angle)/1.8
		#rospy.loginfo(step_count)
		for x in numpy.arange((step_count)):
			 GPIO.output(DIR, GPIO.HIGH)
			 GPIO.output(EN, GPIO.LOW)
			 GPIO.output(STEP, GPIO.HIGH)
			 sleep(delay)
			 GPIO.output(STEP, GPIO.LOW)
			 sleep(delay)
	 		 GPIO.output(EN,GPIO.HIGH)
		#sleep(0.005)
		#rospy.loginfo("moving left side towards destination",difference.data) 
	GPIO.output(EN,GPIO.HIGH)
	rospy.loginfo("new location is %f",current_location.data)




	#os.system('python servo.py')
	#subprocess.call(["python","servo1.py"])	#used to execute terminal commands in python file

if __name__=='__main__':
	walk()
GPIO.cleanup()

