import cv2
import threading
import time
from datetime import datetime

rec_length = 60  # 녹화 시간 (초)


# 1분 타이머 스레드 함수
def timer_thread(stop_event):
    global recording
    time.sleep(rec_length)
    stop_event.set()
    recording = False

# 폴더 생성 함수
def makeFolder(now):
    now = datetime.now()
    folderName = now.strftime("%Y%m%d_%H%M분")

# 파일 생성 함수

# 웹캠 캡처 객체 생성
fileName = "C:/Users/SBA/opencvDojang/video.mp4"
cap = cv2.VideoCapture(fileName)

    
# 녹화 설정
fourcc = cv2.VideoWriter_fourcc(*'XVID')  # 코덱 설정
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = int(cap.get(cv2.CAP_PROP_FPS))  # 프레임 레이트 설정
segment_count = 1
recording = True

while True:
    stop_recording = threading.Event()
    timer = threading.Thread(target=timer_thread, args=(stop_recording,))
    timer.start()
    recording = True
    out = cv2.VideoWriter("C:/Users/SBA/test/output{}.avi".format(segment_count), fourcc, fps, (width, height))  # 출력 파일 설정

# 녹화 시작 

    while recording:
        ret, frame = cap.read()
        if not ret:
            recording = False  # 영상이 끝나면 녹화 중지
            break

        out.write(frame)
        cv2.imshow('blackbox', frame)

        if cv2.waitKey(20) == 27:
            recording = False  # 'Esc' 키 누르면 녹화 중지

        if stop_recording.is_set():
            recording = False  # 타이머 완료 시 녹화 중지
            
      
    out.release()
    timer.join()
    segment_count += 1
    
    if cv2.waitKey(1) == 27 or not ret:
        break

cap.release()
cv2.destroyAllWindows()
