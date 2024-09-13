import cv2
import numpy as np

# 좌표를 저장할 리스트
pt_list = []
shift_pressed = False  # Shift 키 상태를 추적

# 마우스 콜백 함수
def mouse_callback(event, x, y, flags, param):
    global pt_list, shift_pressed
    
    # Shift 키가 눌린 상태에서 마우스 왼쪽 버튼 클릭 시 좌표 저장
    if event == cv2.EVENT_LBUTTONDOWN and (flags & cv2.EVENT_FLAG_SHIFTKEY):
        pt = (x, y)
        pt_list.append(pt)
        print(f"좌표 추가: {pt}")

# 빈 이미지 생성
img = np.ones((512, 512, 3), np.uint8) * 255

# 창 설정 및 마우스 콜백 연결
cv2.namedWindow('img')
cv2.setMouseCallback('img', mouse_callback)

# 메인 루프
while True:
    # 이미지를 계속해서 보여줌
    cv2.imshow('img', img)
    
    # 키보드 입력 감지
    key = cv2.waitKey(1) & 0xFF

    # Shift 키가 눌린 상태 감지
    if key == 16:  # Shift 키의 코드
        shift_pressed = True
    
    # Shift 키가 떼어진 순간 다각형을 그림
    elif shift_pressed and key != 16:
        shift_pressed = False  # Shift 키 떼기
        if len(pt_list) > 1:
            cv2.polylines(img, [np.array(pt_list)], isClosed=True, color=(0, 0, 0), thickness=1)
            cv2.imshow('img', img)  # 이미지 업데이트
            print("폴리라인 그리기 완료")
            pt_list = []  # 좌표 리스트 초기화

    # 'q' 키를 누르면 프로그램 종료
    if key == ord('q'):
        break

cv2.destroyAllWindows()
