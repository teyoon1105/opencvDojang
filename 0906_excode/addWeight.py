# 두 영상 파일을 합성할 때
# 각각 영상의 가중치를 얼마나 둘 지를 정하는 파일

import cv2
import numpy as np

src1 = cv2.imread('data2/airplane.bmp')
src2 = cv2.imread('data2/field.bmp')

alpha = 0.8
beta = 1 - alpha
# 색상은 b, g, r 각각 100씩 더해준다
dst1 = cv2.addWeighted(src1, alpha=alpha, src2=src2, beta=beta, gamma=0)
# dst2= np.clip(src+100, 0, 255).astype(np.uint8)


cv2.imshow('img1', src1)
cv2.imshow('img2', src2)
cv2.imshow('dst1', dst1)
# cv2.imshow('dst2', dst2)
cv2.waitKey()
cv2.destroyAllWindows()