import cv2, sys
import matplotlib.pyplot as plt

fileName = 'data2/raining.mp4'

cap = cv2.VideoCapture(fileName)

if not cap.isOpened():
    sys.exit('video load failed')
    
while(True):
    ret, frame = cap.read()
    frame1 = cv2.add(frame, (50,50,50))
    frame2 = cv2.normalize(frame, None, 0, 255, cv2.NORM_MINMAX)
    frame3 = cv2.Canny(frame, 40, 120)
    frame4 = cv2.bilateralFilter(frame, -1, 10, 5)
    if not ret:
        break
    
    cv2.imshow('raining', frame) 
    cv2.imshow('bright_raining', frame1)
    cv2.imshow('normalize_raining', frame2)
    cv2.imshow('canny_raining', frame3)
    cv2.imshow('bilater_raining', frame4)
    key = cv2.waitKey(40)
    
    if key == 27:
        break
    
    
if cap.isOpened():
    cap.release
    
cv2.destroyAllWindows()