import cv2
import numpy as np
img = np.full((400,400,3), 255, np.uint8)

# 사각형 출력
pt1 = (50,100)
pt2 = (img.shape[0]-50, 100)
pt3 = (img.shape[0]-50, 300)
pt4 = (200,300)
lineColor = (0,0,255)
lineColor2 = (255,0,0) 
thick = 3
lineType = cv2.LINE_AA

# (x1, y1),(x2,y2) 를 통해 사각형 그리기
cv2.rectangle(img, pt1, pt3, lineColor, thick, lineType)

# x,y,w,h를 통해 사각형 그리기
cv2.rectangle(img, (50,100, 100, 100), lineColor2, thick, lineType)

cv2.imshow('img', img)
cv2.waitKey()
cv2.destrotWindow('img')