import cv2, sys
import matplotlib.pyplot as plt
import numpy as np

src1 = cv2.imread("C:/Users/SBA/opencvDojang/misson/01.png")
src2 = cv2.imread("C:/Users/SBA/opencvDojang/misson/misson_image01.png")
if src1 is None or src2 is None:
    sys.exit('image load failed')

# 노이즈 제거
# 하늘을 좀 부드럽게 
# 모든 인자값 기본갑으로 설정
dst1 = cv2.fastNlMeansDenoisingColored(src1, None, 10, 10, 7, 21)

# 사진을 좀 어둡게
# 대신 채도는 높혀서 선명하게
# hsv 채널 분리
hsv_dst = cv2.cvtColor(dst1, cv2.COLOR_BGR2HSV)
h, s, v = cv2.split(hsv_dst)

# 채도는 증가시키기
s = cv2.convertScaleAbs(s, beta = 30)

# 밝기 좀 낮추기
v = cv2.convertScaleAbs(v, beta = -20)


# meger로 hsv  함수 합치기
hsv_dst = cv2.merge((h,s,v))

result = cv2.cvtColor(hsv_dst, cv2.COLOR_HSV2BGR)

cv2.imshow('src2', src2)
cv2.imshow('result', result)
cv2.waitKey()
cv2.destroyAllWindows()