import cv2, sys
import matplotlib.pyplot as plt
import hist_func
# 히스토그램 함수

src = cv2.imread("C:/Users/SBA/opencvDojang/data/srcThreshold.png", cv2.IMREAD_GRAYSCALE)

if src is None:
    sys.exit('image load failed')

# src의 히스토그램
hist_func.hist_gray(src)

# threshold 함수를 이용해서 흑과 백으로 나눈다
src_th = cv2.adaptiveThreshold(src,255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 51, 7)
cv2.imshow('src', src)
cv2.imshow('src_th', src_th)
cv2.waitKey()
cv2.destroyAllWindows()

