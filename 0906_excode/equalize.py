import cv2, sys
import numpy as np
from matplotlib import pyplot as plt
src = cv2.imread('data2/Hawkes.jpg', cv2.IMREAD_GRAYSCALE)

if src is None:
    sys.exit('image load failed')

dst = cv2.equalizeHist(src)


# hist1 = cv2.calcHist([src],[0], None, [256], [0,256])
# hist2 = cv2.calcHist([dst],[0], None, [256], [0,256])
   
    
# dst = cv2.equalizeHist(src)


cv2.imshow('src', src)
cv2.imshow('dst', dst)
# plt.plot(hist1, color = 'r')
# plt.plot(hist2, color = 'b')
# plt.show()
cv2.waitKey()
cv2.destroyAllWindows()
