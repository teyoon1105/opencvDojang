# opencv 환경에서 사진, 창위에 사각형 출력하기
import cv2
import numpy as np
# 사각형의 경우 두가지 방법을 통해 출력이 가능하다
# 첫번째의 경우 대각선을 이룰 수 있는 두 점의 좌표를 설정하면
# 두 좌표의 x값의 차, y값의 차를 각 변으로하는 직사각형을 만들어준다
#cv2.rectangle(img, pt1, pt2, color, thickness, lineType, shift)
# pt1, pt2 : 대각의 관계를 갖고 있는 두 점의 좌표
# color : 선 색
# thickness : 선 두께
# lineType : 선 타입
# shift : 그리기 과표 값의 축소 비율
# 빈 창 생성
img = np.full((400,400,3), 255, np.uint8)
# 대각 점 설정
pt1 = (50,100)
pt2 = (img.shape[0]-50, 300)
# 선 색
color = (255,0,0)
# 선 굵기
thick = 2
# 선 타입
lineType = cv2.LINE_AA

# 사각형 출력
cv2.rectangle(img, pt1, pt2, color, thick, lineType)

# 두번째 방법은 사각형이 시작될 위치와 너비 높이를 지정하는 방법이다
#cv2.rectangle(img, rec, color, thick, lineType, shift)
# rec : 사각형의 위치정보(x, y, w, h)

rec = (50, 100, 200, 300)
color2 = (0,0,255)
cv2.rectangle(img, rec, color2, thick, lineType)

cv2.imshow('img', img)
cv2.waitKey()
cv2.destrotWindow('img')