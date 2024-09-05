import cv2
import numpy as np
img = np.full((400,400,3), 255, np.uint8)

# 직선 출력
pt1 = (50,100)
pt2 = (img.shape[0]-50, 100)
pt3 = (img.shape[0]-50, 300)
lineColor = (0,0,0)
thick = 3
lineType = cv2.LINE_8
cv2.line(img, pt1, pt2, lineColor, thick, lineType)
cv2.line(img, pt1, pt3, lineColor, thick, lineType)
cv2.line(img, pt2, pt3, lineColor, thick, lineType)

cv2.imshow('img', img)
cv2.waitKey()
cv2.destrotWindow('img')