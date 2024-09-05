import cv2, sys

cap = cv2.VideoCapture(0)

print(int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)), \
    int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)))

if cap.isOpened():
    cap .release()