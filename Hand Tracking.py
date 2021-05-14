# pip install cvzone
# pip install opencv-contrib-python

import cvzone
import cv2
cap = cv2.VideoCapture(1)
detector = cvzone.HandDetector(detectionCon=0.5, maxHands=2)
while True:
    success, img = cap.read()
    img = cv2.flip(img,1)
    img = detector.findHands(img)
    cv2.imshow("Image", img)
    cv2.waitKey(1)