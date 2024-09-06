import cv2, sys
import numpy as np

src = cv2. imread('data2/rose.bmp', cv2.IMREAD_GRAYSCALE)

if src is None:
    sys.exit('image load failed')
    
    
kernel_size = 3
kernel = (kernel_size, kernel_size)
# blur 처리
# (3,3) : 필터의 크기가 3 X 3 배열
dst = cv2.blur(src, kernel = kernel)


cv2.imshow('src', src)
cv2.imshow('dst', dst)
cv2.waitKey()
cv2.destroyAllWindows()