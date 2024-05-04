# Importing modules
import cv2 as cv
import numpy as np
from cvzone.HandTrackingModule import HandDetector
import mediapipe as mp


def startOpenCV():
    # Some Variables
    width = 640
    height = 480

    # Setting up the camera
    cap = cv.VideoCapture(0) #cap is an object for video capturing
    # setting dimensions
    cap.set(4, width)
    cap.set(3, height)

    

    # Hand Detector
    detector = HandDetector(detectionCon = 0.8, maxHands = 1)

    
    ############### READING WEBCAM ##########################
    while True:
        success, img = cap.read()
        cv.imshow("Image", img)

    
        # Keyboard input check
        key = cv.waitKey(1)    
        if key == ord('q'):
            break

        # detect hand
        hands, img = detector.findHands(img)

        if hands:
            hand = hands[0]
            fingers = detector.fingersUp(hand)
            # Detecting if only one finger up
            if fingers.count(1) == 1:
                print('Only one')
            print(fingers)
                

startOpenCV()
