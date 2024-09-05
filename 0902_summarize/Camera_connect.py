# 로컬 컴퓨터에 설치된 웹캠에 접근하는 방법
# cv2, sys패키지 불러오기

import cv2, sys

# VideoCapture객체를 생성할 때 (0)을 입력하면 로컬pc에 연결된
# 카메라에 접근할 수 있음
cap = cv2.VideoCapture(0)