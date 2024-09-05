# inRange()함수를 잘 설정하려면 trackBar 기능이 필요하다
import cv2, sys
import numpy as np

# 트랙바 함수 생성
def on_trackbar(pos):
    hmin = cv2.getTrackbarPos('H_min', 'Trackbar')
    hmax = cv2.getTrackbarPos('H_max', 'Trackbar')
    smin = cv2.getTrackbarPos('S_min', 'Trackbar')
    smax = cv2.getTrackbarPos('S_max', 'Trackbar')
    vmin = cv2.getTrackbarPos('V_min', 'Trackbar')
    vmax = cv2.getTrackbarPos('V_max', 'Trackbar')
    dst = cv2.inRange(src_hsv, (hmin,smin,vmin), (hmax,smax,vmax))
    cv2.imshow('trackbar', dst)
    
#src = cv2.imread("C:/Users/SBA/opencvDojang/data2/red.jpg")
src = cv2.imread("C:/Users/SBA/opencvDojang/data2/green.jpg")
#src = cv2.imread("C:/Users/SBA/opencvDojang/data2/yellow.jpg")
if src is None:
    sys.exit('image load failed')
    
# 색상의 범위를 잘 지정하려면 bgr>hsv
src_hsv = cv2.cvtColor(src, cv2.COLOR_BGR2HSV)

# 창에 트랙바를 넣기 위해서는 창을 먼저 생성
cv2.namedWindow('Trackbar')
cv2.imshow('Trackbar', src)

# 트랙바 생성
# H_min, H_max : 트랙바 이름
# 0, 255 : 범위
# 트랙바를 움직일 때  호출되는 함수(콜백함수)
cv2.createTrackbar('H_min', 'Trackbar', 0, 255, on_trackbar)
cv2.createTrackbar('H_max', 'Trackbar', 0, 255, on_trackbar)
cv2.createTrackbar('S_min', 'Trackbar', 0, 255, on_trackbar)
cv2.createTrackbar('S_max', 'Trackbar', 0, 255, on_trackbar)
cv2.createTrackbar('V_min', 'Trackbar', 0, 255, on_trackbar)
cv2.createTrackbar('V_max', 'Trackbar', 0, 255, on_trackbar)
on_trackbar(0)

cv2.waitKey()
cv2.destroyAllWindows() 
    