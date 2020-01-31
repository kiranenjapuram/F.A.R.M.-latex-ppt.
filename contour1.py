"""
Project Name: Farming with Autonomous Robotic system usning Machine   
Author List: Akshaya Naik ,Shraddha Gaikwad
Filename:contour1.py
Functions: none
Global Variables: None

"""


import numpy as np
import cv2


##live feed reading by camera.
im = cv2.imread('Image_plant_for_detection.jpg') ###location of saved image from feed of go_to_location. 
#im=cv2.resize(img,(600,600))



##converting RGB to HSV.
hsv_img = cv2.cvtColor(im, cv2.COLOR_BGR2HSV)
#viewimage(hsv_img)

COLOR_MIN = np.array([40,100,50],np.uint8)
COLOR_MAX = np.array([80, 255, 255],np.uint8)
frame_threshed = cv2.inRange(hsv_img, COLOR_MIN, COLOR_MAX)
imgray = frame_threshed


##setting threshold for feed.
ret,thresh = cv2.threshold(frame_threshed,127,255,0)
_,contours,_ = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

# Find the index of the largest contour
areas = [cv2.contourArea(c) for c in contours]
max_index = np.argmax(areas)
cnt=contours[max_index]


print(len(contours))


##detecting the plant by rectangle.
x,y,w,h = cv2.boundingRect(cnt)
cv2.rectangle(im,(x,y),(x+w,y+h),(0,255,0),2)
cv2.imshow("Show",im)
cv2.waitKey()
cv2.destroyAllWindows()
