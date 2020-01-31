#!/usr/bin/env python

"""
Project Name: Farming with Autonomous Robotic system usning Machine   
Author List: shreya jagtap , Chinmay Lokare
Filename: QR_detection_decoding_pyzbar.py
Functions: none
Global Variables: None

"""
from pyzbar import pyzbar
import cv2



##initialisation of camera.
cap=cv2.VideoCapture(0)
while True:
        ref,image=cap.read(0)
        barcodes=pyzbar.decode(image)
        for barcode in barcodes:
                    ##executing the for loop.
                    (x,y,w,h)=barcode.rect

                    cv2.rectangle(image,(x,y),(x+w,y+h),(255,0,0),2)

                    barcodeData=barcode.data.decode()

                    barcodeType=barcode.type



                    text="{} ({})".format(barcodeData,barcodeType)

                    cv2.putText(image,text,(x,y-10),cv2.FONT_HERSHEY_SIMPLEX,0.5,(0,0,255),2)

        ##displaying the results.
        cv2.imshow("Image",image)
        # checking for exit key
        KeyPressed = cv2.waitKey(2)
        if KeyPressed ==ord('q'):
                break
cv2.VideoCapture.release()
cv2.destroyAllWindows()
