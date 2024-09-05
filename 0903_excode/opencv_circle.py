import cv2
import numpy as np
img = np.full((400,400,3), 255, np.uint8)

# 원 그리기
cv2.circle(img, (int(img.shape[0]/2), int(img.shape[1]/2)), 100, (0,255,0), 3, cv2.LINE_AA) 

cv2.imshow('img', img)
cv2.waitKey()
cv2.destroyWindow('img')