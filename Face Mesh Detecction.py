# pip install cvzone
# pip install opencv-contrib-python

import cvzone
import cv2
cap = cv2.VideoCapture(1)
detector = cvzone.FaceMeshDetector(maxFaces=1)
while True:
    success, img = cap.read()
    img = cv2.flip(img,1)
    img, faces = detector.findFaceMesh(img)
    if faces:
        print(faces[0])
        cv2.imshow("Image", img)
        cv2.waitKey(1)