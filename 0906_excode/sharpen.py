import cv2, sys
import numpy as np
from matplotlib import pyplot as plt
# cartoon filter
src = cv2. imread('data/Lena.bmp')

if src is None:
    sys.exit('image load failed')
    
dst = cv2.bilateralFilter(src, -1, 10, 5)

hist1 = cv2.calcHist([src], [0], None, [256], [0,256])
hist2 = cv2.calcHist([dst], [0], None, [256], [0,256])

cv2.imshow('src', src)
cv2.imshow('dst', dst)
plt.plot(hist1, color = 'r')
plt.plot(hist2, color = 'b')
plt.show()
cv2.waitKey()
cv2.destroyAllWindows()