import cv2, sys
import numpy as np
import matplotlib.pyplot as plt

# 이미지를 불러오기
src = cv2.imread("C:/Users/SBA/opencvDojang/misson/01.png")

if src is None:
    sys.exit('image load failed')
    
# 히스토그램
colors = ['b', 'g', 'r']
bgr_planes = cv2.split(src)

# for  (p,c) in zip(bgr_planes, colors):
#     hist = cv2.calcHist([p], [0], None, [256], [0, 256])
#     plt.plot(hist, color=c)

# plt.show()


# YCbCr 채널을 활용
# BGR 에서 YCbCr로
src_Ycc = cv2.cvtColor(src, cv2.COLOR_BGR2YCrCb)
hist1 = cv2.calcHist([src_Ycc], [0], None, [256], [0,256])
plt.plot(hist1)


Y, Cb, Cr = cv2.split(src_Ycc)

# src_Ycc에 normalize적용
# src_norm = cv2.normalize(src_Ycc, None, 0 ,255, cv2.NORM_MINMAX)
# 분리된 채널 Y에 normalize 적용
# 최소와 최대값이 존재 > normalize 안됨
# Y_norm = cv2.normalize(Y, None, 0 ,255, cv2.NORM_MINMAX)
# hist2 = cv2.calcHist([Y_norm], [0], None, [256], [0,256])

# Y값에 50정도 더해줌, 휘도 증가, 밝기 증가
Y_add = cv2.add(Y,50)
hist3 = cv2.calcHist([Y_add], [0], None, [256], [0,256])
plt.plot(hist3)
plt.show()

# Y에 equalize 적용
# Y_equal = cv2.equalizeHist(Y)
# hist3 = cv2.calcHist([Y_equal], [0], None, [256], [0,256])
# plt.plot(hist3)
# plt.show()

# src_Ycc_equal = cv2.merge((Y_add, Cb, Cr))
# src_equal = cv2.cvtColor(src_Ycc_equal, cv2.COLOR_YCrCb2BGR)
# cv2.imshow('src', src)
# cv2.imshow('src_equal', src_equal)
# cv2.waitKey()
# cv2.destroyAllWindows()

src_Ycc_add = cv2.merge((Y_add, Cb, Cr))
src_add = cv2.cvtColor(src_Ycc_add, cv2.COLOR_YCrCb2BGR)
cv2.imshow('src', src)
cv2.imshow('src_equal', src_add)
cv2.waitKey()
cv2.destroyAllWindows()


