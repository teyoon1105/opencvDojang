import cv2, sys
import numpy as np

src = cv2.imread('data2/road.png', cv2.IMREAD_GRAYSCALE)

if src is None:
    sys.exit('image load failed')
    
    
dst = cv2.Canny(src,80, 120)


cv2.imshow('src', src)
cv2.imshow('dst', dst)
cv2.waitKey()
cv2.destroyAllWindows()
