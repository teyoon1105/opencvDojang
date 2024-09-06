import cv2, sys
import matplotlib.pyplot as plt
import numpy as np

src = cv2.imread('data2/candies.png', cv2.IMREAD_GRAYSCALE)
dst = cv2.add(src, 50)

hist1 = cv2.calcHist([src], [0], None, [256], [0,256])
hist2 = cv2.calcHist([dst], [0], None, [256], [0,256])

plt.plot(hist1)
plt.plot(hist2)
plt.show()
