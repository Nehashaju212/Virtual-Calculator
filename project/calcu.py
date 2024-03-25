import cv2
from cvzone.HandTrackingModule import HandDetector
cap = cv2.VideoCapture(1)
while True:
    success, img = cap.read()
    img = cv2.flip(img, 1)
    cv2.imshow("image",img)
    cv2.waitKey(1)
