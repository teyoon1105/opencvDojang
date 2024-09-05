# 이미지를 불러올 때는 imread()
# 동영상을 불러올 때는 VideoCapture()
import cv2, sys


fileName = 'data/vtest.avi'

# VideoCapture 객체 생성, 생성자 호출(파일열기) 
cap = cv2.VideoCapture(fileName)

# 동영상의 정보(해상도, width, frame, height)를 가져오는 법
# print(int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)))
# print(int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))) 
# print(int(cap.get(cv2.CAP_PROP_FPS))) 

framesize = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)), \
    int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    
#  동영상 이미지를 다 가져올 때 까지 반복
while(True):
    # 동영상에서 한장의 이미지를 가졍오기
    # retval : 동영상에서 이미지 가져올 때 정상 동작을 했나?
    # 정상 : True, 비정상 : False
    # frame : 이미지 한장
    # 동영상 코덱 디코딩도 포함
    retval, frame = cap.read()
    # retval가 양수가 아니면  while문 빠져나가기
    if not retval:
        break
    cv2.imshow('frame', frame)
    
    # 100ms 대기, 이 동영상은 초당 10프레임, 0.1초당 1frame이기 때문
    key = cv2.waitKey(100)
    # key 입력이 27(esc)라면 종료
    if key == 27:
        break
    
#  동영상을 열었으면, 닫아야 한다.
if cap.isOpened():
    cap.release() # 열림 해제
    
cv2.destroyAllWindows()
    