import cv2, sys
import numpy as np
from matplotlib import pyplot as plt
src = cv2.imread('data2/Hawkes.jpg', cv2.IMREAD_GRAYSCALE)

if src is None:
    sys.exit('image load failed')

dst1 = cv2.equalizeHist(src)

dst2 = cv2.normalize(src, None, 0, 255, cv2.NORM_MINMAX)

hist1 = cv2.calcHist([src],[0], None, [256], [0,256])
hist2 = cv2.calcHist([dst1],[0], None, [256], [0,256])
hist3 = cv2.calcHist([dst2],[0], None, [256], [0,256])
   
    

cv2.imshow('src', src)
cv2.imshow('dst1', dst1)
cv2.imshow('dst2', dst2)
plt.plot(hist1, color = 'r')
plt.plot(hist2, color = 'b')
plt.plot(hist3, color = 'g')
plt.show()
cv2.waitKey()
cv2.destroyAllWindows()