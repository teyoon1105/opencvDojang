# 웹캠에서 들어오는 영상을 녹화해서 파일로 저장
# 혹은 원래 있는 동영상을 녹화해서 파일로 저장

# 패키지 불러오기
import cv2, sys

# 웹캠, 원래 있는 동영상 사용하는 조건을 걸어야 하기에
isWEBCAM = False
if isWEBCAM == True:
    # 웹캠이라면 사용할 카메라 지정
    cap = cv2.VideoCapture(0)
    
else:
    # 아니라면 사용할 동영상 파일 경로 저장
    fileName = 'data/vtest.avi'
    cap = cv2.VideoCapture(fileName)

# 녹화를 하기 위해 필요한, frame사이즈, fps 값들을 변수로 저장
# 카메라, 동영상의 frame 불러오기
frame_size =  (int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)), \
    int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)))

# fps 값 불러오기
fps = int(cap.get(cv2.CAP_PROP_FPS))

# 코덱 설정, 압축, 압축 해제에 관련
fourcc = cv2.VideoWriter_fourcc(*'XVID')

# 컬러 동영상 녹화, 압축, 저장
out1 = cv2.VideoWriter('data/myrecord0.mp4',fourcc, fps, frame_size)
# gratscale 동영상 녹화, 압축, 저장
out2 = cv2.VideoWriter('data/myrecord1.mp4',fourcc, fps, frame_size,isColor=False)

# 이제 웹캠 혹은 비디오 영상을 한 frame씩 불러와야 함
while(True):
    
    retval, frame = cap.read()
    
    # 제대로 불러왔는지 확인
    if not retval:
        break
    # 동영상 녹화, 저장에 프레임을 전달
    out1.write(frame)
    grayFrame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    out2.write(grayFrame)

    # 잘 녹화가 되는지 영상 출력
    cv2.imshow('frame', frame)
    cv2.imshow('gray', grayFrame)
    
    # 마찬가지로 한 프레임이 지나가기 전까지 키 입력 기다림
    delay = int(1000/fps)
    
    if cv2.waitKey(delay) == 27:
        break
    
# 모든 frame이 전달되거나, esc를 눌러 while문을 빠져나옴
# 창, 영상, 녹화기 전부 종료
cap.release()
out1.release()
out2.release()
cv2.destroyAllWindows()