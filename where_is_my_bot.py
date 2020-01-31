#!/usr/bin/env python



"""
Project Name: Farming with Autonomous Robotic system usning Machine   
Author List: Kiran Enjapuram ,Ajinkya Giri , Chinmay Lokare
Filename: Where_is_my_bot.py
Functions: p_publisher.
Global Variables: None

"""


from pyzbar import pyzbar
import cv2
import sys
from pyzbar import pyzbar
import argparse

import numpy as np
#import subprocess


import rospy

from sensor_msgs.msg import Image
from sensor_msgs.msg import CameraInfo

#import camera_info_manager
from std_msgs.msg import Float64
from std_msgs.msg import String

from cv_bridge import CvBridge, CvBridgeError




cap=cv2.VideoCapture(0)


"""
Function Name: p_publisher
Input: takes distance of the destination at which system should reach.
Output: publishes the data in topic distance_topic_2 which is desired location of system.
Logic: this will run the publisher node and shows the video feed and publish dostance data on topic bot_position.

""" 


def p_publisher():
		#rospy.init_node('image_converter', anonymous=True)
		rospy.init_node('where_is_my_bot', anonymous=True)

		#image_pub = rospy.Publisher("image_topic_2",Image)
		position_pub = rospy.Publisher("bot_position",Float64,queue_size=1)

		#bridge = CvBridge()
		while True:
			ref,img=cap.read(0)
			cv2.imwrite("Image_plant_for_detection.jpg",img)

			if ref:
				# adding variables for localization calculation
				Localization_variable = ()
				NumQRtags = 0
				# getting the QR objects from image
				barcodes=pyzbar.decode(img)
				for barcode in barcodes:
					    NumQRtags += 1
					    (x, y, w, h) = barcode.rect
                                            cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
					    barcodeData = barcode.data.decode()
					    barcodeType = barcode.type
					    Location = (round((x + w/2) ), round((y + h/2)))
					    QRobject = Location + (int(barcodeData),)
					    Localization_variable = Localization_variable + (QRobject,)
					    #text = "{} ({})".format(barcodeData, barcodeType)
					    text = "{} cm".format(barcodeData)
					    cv2.putText(img, text, (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)
				Localization_variable = (NumQRtags,) + Localization_variable
				Center=img.shape
				cX=int(Center[1]/2)
				cY=int(Center[0]/2)
				#print(Center[0]/2)
				#print(cX)
				cv2.putText(img,'+',(cX,cY),cv2.FONT_HERSHEY_SIMPLEX,0.5,(0,0,255),4)
				# checking num of QR and selecting the technique
                                if NumQRtags==0:
                                	print("No QR tag detected.")
				elif NumQRtags==1:
					# only one QR tag detected
					print("1 QR tag detected not enough. Find more QR tag")
				else:
					if NumQRtags==2:

						# calculating object distance assuming only two QR tags are in image
						QR_left_location = Localization_variable[1][0]
						QR_Right_location = Localization_variable[2][0]
						QR_left_distance = Localization_variable[1][2]
						QR_Right_distance = Localization_variable[2][2]
						#print(QR_left_distance)
						#print(QR_Right_distance)
						Object_location = cX
						Object_distance = ((Object_location - QR_Right_location) * (QR_left_distance - QR_Right_distance) / (
						QR_left_location - QR_Right_location)) + QR_Right_distance
						Object_distance=round(Object_distance,2)
						#print(Object_distance)
						#distance_pub.publish(Object_distance)
						rospy.loginfo(Object_distance)
						position_pub.publish(Object_distance)
						#print(text)
				# displaying video feed
				cv2.imshow("Video Feed",img)

				# checking for exit key
				KeyPressed = cv2.waitKey(10)
				if KeyPressed ==ord('q'):
					break



if __name__=='__main__':
    try:
        p_publisher()
    except rospy.ROSInterruptException:
        pass
