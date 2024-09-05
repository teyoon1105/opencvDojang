import cv2, sys
import numpy as py

def on_trackbar(pos):
    global hsv
    hmin = cv2.getTrackbarPos('H_min', 'frame')
    hmax = cv2.getTrackbarPos('H_max', 'frame')

    mask = cv2.inRange(hsv,(hmin,150,0),(hmax,255,255))
    cv2.copyTo(frame2, mask, frame1)
    cv2.imsho('frame', frame1)
          

rain = "data2/raining.mp4"

woman = "data2/woman.mp4"

cap1 = cv2.VideoCapture(woman)
cap2 = cv2.VideoCapture(rain)


if not cap1.isOpened():
    print('video1 open failed')
    sys.exit()
    
if not cap2.isOpened():
    print('video2 open failed')
    sys.exit()
    
fps1 = int(cap1.get(cv2.CAP_PROP_FPS))
fps2 = int(cap2.get(cv2.CAP_PROP_FPS))

frameCount1 = int(cap1.get(cv2.CAP_PROP_FRAME_COUNT))
frameCount2 = int(cap2.get(cv2.CAP_PROP_FRAME_COUNT))

# print(fps1)
# print(fps2)

# print(frameCount1)
# print(frameCount2)

delay = int(1000/fps1)

# 합성 여부 설정 플래그
do_composite = False


cv2.namedWindow('frame')
cv2.createTrackbar('H_min', 'frame', 40, 60, on_trackbar)
cv2.createTrackbar('H_max', 'frame', 60, 80, on_trackbar)
on_trackbar(0)

ret1, frame1 = cap1.read()
hsv = cv2.cvtColor(frame1, cv2.COLOR_BGR2HSV)

while True:
    ret1, frame1 = cap1.read()
    if not ret1:
        break
    
    ret2, frame2 = cap2.read()
    if do_composite:
        # hsv 색공간에서 영역을 검출해서 합성
        hsv = cv2.cvtColor(frame1, cv2.COLOR_BGR2HSV)
        mask = cv2.inRange(hsv,(50,150,0),(70,255,255))
        cv2.copyTo(frame2, mask, frame1)
        
    
    cv2.imshow('frame', frame1)
    key = cv2.waitKey(delay)
    
    # 스페이스 바를 눌렀을 때 do_composite를 반전시킨다
    if key == ord(' '):
        do_composite = not do_composite
        # ESC키를 누르면 종료
    elif key == 27:
        break
        
    
cap1.release()
cap2.release()
cv2.destroyAllWindows()
    
    