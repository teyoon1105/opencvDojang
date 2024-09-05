# opencv 환경에서 사진, 창 위에 직선 그리기

import cv2
import numpy as np

# cv2.line(img, pt1, pt2, color, thickness, lineType, shift)

# pt1 : 선분을 그리기 시작할 시작점
# pt2 : 선분을 끝맺을 끝점
# color : 색 선
# thickness : 선 두께
# lineType : 선 타입
# shit : 그리기 좌표 값의 축소 비율

# 빈 창 만들기
img = np.full((400,400,3), 255, np.uint8)

# 시작점 끝 점 설정
pt1 = (50,100)
pt2 = (img.shape[0]-50,100)

# 색 선 선택
color = (255,0,0)

# 선 두께 선택
thick = 1

# 선 타입 선택
lineType = cv2.LINE_8

# 선 그리기
cv2.line(img, pt1, pt2, color, thick, lineType)

cv2.imshow('img', img)
cv2.waitKey()
cv2.destroyAllWindows()