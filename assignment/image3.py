import cv2, sys
import matplotlib.pyplot as plt
import numpy as np


# 파일을 가져온다
# src1 사진을 src2 사진처럼 필터링하기
src1 = cv2.imread("C:/Users/SBA/opencvDojang/misson/05.png")
src2 = cv2.imread("C:/Users/SBA/opencvDojang/misson/misson_image05.png")

# 미션 사진이 좀 더 어둡고, 선명해보임

# 원본 사진의 색 채널 나누기
hsv_src = cv2.cvtColor(src1, cv2.COLOR_BGR2HSV)
h, s, v = cv2.split(hsv_src)

# 채도 증가시키기
s = cv2.convertScaleAbs(s, beta = 20)

# 밝기 좀 낮추기
v = cv2.convertScaleAbs(v, beta = -20)

# meger로 hsv  함수 합치기
hsv_scr = cv2.merge((h,s,v))

dst = cv2.cvtColor(hsv_scr, cv2.COLOR_HSV2BGR)

cv2.imshow('mission', src2)
cv2.imshow('result', dst)
cv2.waitKey()
cv2.destroyAllWindows()