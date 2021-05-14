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
    lmList, bbox = detector.findPosition(img, draw=False)
    if lmList:
        myHandType = detector.handType()
        cv2.putText(img, myHandType, (50, 50), cv2.FONT_HERSHEY_PLAIN, 2, (0, 255, 0), 2)
    cv2.imshow("Image", img)
    cv2.waitKey(1)