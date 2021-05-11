import cvzone
import cv2
cap = cv2.VideoCapture(0)
detector = cvzone.FaceDetector()
while True:
    success, img = cap.read()
    img = cv2.flip(img, 1)
    # Face Detection
    img, bboxs = detector.findFaces(img)
    cv2.imshow("Image", img)
    cv2.waitKey(1)

