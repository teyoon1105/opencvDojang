# 이미지를 불러오는 함수는 imread()
# 동영상을 불러오는 함수는 VideoCapture()

# 패키지 불러오기
import cv2, sys

# 파일 경로 저장
fileName = 'data/vtest.avi'

# VideoCapture 객체를 생성, 생성자 호출(파일열기)
cap = cv2.VideoCapture(fileName)

# 동영상의 정보확인
# cap.get(cv2.CAP_PROP_FRAME_WIDTH), 프레임 너비
# cap.get(cv2.CAP_PROP_FRAME_HEIGHT), 프레임 높이
# cap.get(cv2.CAP_PROP_FPS), 프레임 속도

# 동영상은 결국 수많은 사진의 연속
# 각 사진을 불러온다
while(True):
    retval, frame = cap.read()
    # frame을 파일에서 불러오고
    # 제대로 불러왔다면 True, 불러오지 못했다면 False를 반환하는
    # retval 역시 불러온다.
    
    # 전부다 불러왔거나 하나라도 못 불러왔다면
    # frame을 불러오는 while문을 탈출
    if not retval:
        break
    
    # 불러온 frame을 창을 통해 출력
    cv2.imshow('frame', frame)
    
    # 창을 닫을 수 있게 waitKey()함수를 사용
    key = cv2.waitKey(100)
    # 100밀리세컨드를 기달린다
    # 해당 영상이 fps = 10, 즉 1초당 10프레임이기 때문에
    # 1프레임당 0.1초, 100ms이기 때문에
    # 한 프레임이 지나갈 때까지 키 입력을 기다리겠다는 의미이다.
    
    # 27은 esc 키를 의미함
    if key ==27:
        break
    # 동영상 파일을 열었으니 다시 닫아줘야 한다
    
    
if cap.isOpened():
    cap.release
        
    # 동영상을 닫았으니 창 역시 닫아준다
    
cv2.destroyAllWindows()
    