import os
import cv2
import threading
import time
from datetime import datetime

recording = True
# 60초를 지연시키는 스레드를 만들기 위해 설정한 변수
rec_length = 60

# 60초를 지연시키는 스레드
def timer_thread(stop_event):
    global recording
    # loop = rec_length
    # 녹화를 시작하면 recording = True값 반환하게 하여
    # 해당 while문 안에 들어갈 수 있게 만듦
    # while(recording):
        # 1초를 쉬는 함수
        # time.sleep(1)
        # # 원래 loop 값은 60
        # # 1초 쉬면 loop 값 -1을 해서 총 60초 쉬게 만드는 함수
        # loop -= 1
        # if loop == 0:
        #     break
    # 1분 녹화를 하면 녹화를 중지하게 이벤트를 설정
    time.sleep(60)
    stop_event.set()
    recording = False
# 입력으로 원본비디오 파일경로, 츨력폴더, 분할 시간을 받는 함수
def record_video(fileName, output_dir='segments', segment_length=60):
    global recording
    cap = cv2.VideoCapture(fileName)
    if not cap.isOpened():
        print('Error : cannot open video file')
        return
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    fps = int(cap.get(cv2.CAP_PROP_FPS))
    frame_size = (int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)), \
    int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)))
    delay = int(1000/fps)
    
    # 분할 된 영상 파일의 번호(우린 파일명을 변화시키는 방법을 사용)
    segment_count = 0
    # 처리중인 프레임 수를 저장하는 변수
    frame_count = 0
    
    # 60초 녹화가 끝나거나 원본 파일이 끝이날 때까지 루프
    while True:
        stop_recording = threading.Event()
        timer = threading.Thread(target=timer_thread, args=(stop_recording,))
        timer.start()
        recording = True
    
        segment_filename = os.path.join(output_dir, f"segment_{segment_count:03d}.avi"
            )
        out = cv2.VideoWriter(segment_filename, fourcc, fps, frame_size)


        while(recording):

            ret, frame = cap.read()
            if not ret:
                break
            out.write(frame)
            cv2.imshow("Video Recording", frame)
            
            key = cv2.waitKey(delay)
            if key == 27:
                recording = False
                
                
            frame_count += 1
            
        out.release()
        timer.join()
        segment_count += 1
        
        
        if not recording:
            break
        
    cap.release()
    cv2.destroyAllWindows()
    
if __name__ == "__main__":
    video_file = "C:/Users/SBA/opencvDojang/video.mp4"  # 녹화할 비디오 파일 경로
    output_folder = "C:/Users/SBA/opencvDojang/test"  # 분할된 영상 저장 폴더 경로

    record_video(video_file, output_folder)
# 녹화 종료        
# cap.release
# out.release
# cv2.destroyAllWindows()
            

    