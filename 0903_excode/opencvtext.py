
import cv2
import numpy as np
img = np.full((400,400,3), 255, np.uint8)

# 문자열 출력
text = 'Hello OPENCV!'
font = cv2.FONT_HERSHEY_SIMPLEX
fontSize = 1
BlueColor = (255,0,0)
thick = 1
lineType = cv2.LINE_AA

cv2.putText(img, text,(50,350), font, fontSize, BlueColor, thick, lineType) 
cv2.imshow('img', img)
cv2.waitKey()
cv2.destrotWindow('img')
