import cv2, sys
import numpy as np

src = cv2. imread('data2/rose.bmp', cv2.IMREAD_GRAYSCALE)

if src is None:
    sys.exit('image load failed')
    
    

# blur 처리
dst1 = cv2.GaussianBlur(src, (0,0),1)
dst2 = cv2.GaussianBlur(src, (0,0),2)
dst3 = cv2.GaussianBlur(src, (0,0),3)

text1 = 'sigma = 1'
text2 = 'sigma = 2'
text3 = 'sigma = 3'

ord = (30,30)
font = cv2.FONT_HERSHEY_SIMPLEX
fontSize = 1
color = (255,0,0)
thick = 3
lineType = cv2.LINE_AA
cv2.imshow('src', src)

cv2.putText(dst1, text1, ord, font, fontSize, color, thick, lineType)
cv2.imshow('dst1', dst1)

cv2.putText(dst2, text2, ord, font, fontSize, color, thick, lineType)
cv2.imshow('dst2', dst2)

cv2.putText(dst3, text3, ord, font, fontSize, color, thick, lineType)
cv2.imshow('dst3', dst3)

cv2.waitKey()
cv2.destroyAllWindows()