# opencv 환경에서 특정 사진 혹은 창에 문자열 그리기
# 문자열을 그리거나, 다른 도형을 그리기 위해선
# 좌표정보가 필요하기 때문에
# numpy 패키지를 사용
import cv2
import numpy as np

# 빈 창(모든 색상을 255,255,255로 설정)
# 400*400 해상도에 색상 채널 3개임, 그 색상 채널 전부 255로 채움, uint8은 0부터 255까지의 정수를 나타내는 부호 없는 8비트 정수형
img = np.full((400,400,3), 255, np.uint8)

# 원하는 문자열
text = 'Hello OPENCV!'

# cv2.putText(img, text, org, fontFace, fontScale, color, thinkness, lineTpye, bottomeLeftOrigin)
# img : 그림을 그릴 창, 사진
# text : 원하는 문자열
# org : 문자열을 출력 시작할 좌표
# fontFace : 폰트 종류, cv2.FONT_HERSHEY_i(상수)
# fontScale : 폰트 크기
# color : 선 색
# thickness : 선 두께, 기본값 1, -1은 내부를 채움
# lineType : 선 타입. cv2.LINE_4,8,AA
# bottomeLeftOrgin : True > 가장 좌측 하단을 원정으로 간주

# 좌표
ord = (50,100)

# 폰트 종류
font = cv2.FONT_HERSHEY_SIMPLEX

# 폰트 크기
fontSize = 1

# 선 색
color = (255,0,0)

# 선 두께
thick = 1

# 선 타입
lineType = cv2.LINE_AA

# 문자열 출력
cv2.putText(img, text, ord, font, fontSize, color, thick, lineType)
cv2.imshow('img', img)
cv2.waitKey()
cv2.destroyAllWindows()