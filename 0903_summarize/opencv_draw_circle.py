# opencv 환경에서 사진, 창 위에 원 그리기
import cv2
import numpy as np

# cv2.circle(img, center, radius, color, thick, lineType, shift)

# center : 원의 중심 좌표
# radius : 원의 반지름 크기
# color : 선색
# thick : 선 두께
# lineType : 선 타입
# shift: 그리기 좌표값의 축소 비율

# 빈창 생성
img = np.full((400,400,3),255,np.uint8)
# 원의 중심
center = (int(img.shape[0]/2), int(img.shape[1]/2))
# 원의 반지름
radius = 100
# 선 색
color = (0,0,255)
# 선 두께
thick = 3
# 선 타입
lineType = cv2.LINE_8

# 원 출력
cv2.circle(img, center, radius, color, thick, lineType)


cv2.imshow('img', img)
cv2.waitKey()
cv2.destroyWindow('img')

