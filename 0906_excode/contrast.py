# cv2.nomalize

import cv2, sys
import numpy as np
from matplotlib import pyplot as plt
# grayscale로 읽어오기
src = cv2.imread('data2/Hawkes.jpg', cv2.IMREAD_GRAYSCALE)

if src is None:
    sys.exit('image load failed')
    

# src이미지에서 최소값과 최대값을 확인, 최대 최소값을 0~255로 늘려서 색을 선명하게 하기 위한 작업
# pixMin, pixMax, _, _ = cv2.minMaxLoc(src)
# print(pixMin, pixMax)

# 이미지 색상을 정규화 한다
dst = cv2.normalize(src, None, 0, 255, cv2.NORM_MINMAX)

hist1 = cv2.calcHist([src], [0], None, [256], [0,256])
hist2 = cv2.calcHist([dst], [0], None, [256], [0,256])
# 데이터 결과를 파일로 저장
cv2.imwrite('data2/Hawkes_norm.jpg', dst)
cv2.imshow('img1', src)
cv2.imshow('img2', dst)
plt.plot(hist1, color = 'r')
plt.plot(hist2, color = 'b')
plt.show()
cv2.waitKey()
cv2.destroyAllWindows()
