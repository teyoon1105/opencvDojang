import cv2, sys
import numpy as np
import matplotlib.pyplot as plt
pt_list_numpy = []
pt_list = []
shift_pressed = False
# 마우스 콜백 함수를 사용하여 원 그리기
def mouse_callback(event, x, y, flags, param):
    global img, pt_list, shift_pressed
    
    # 마우스 오른쪽 버튼 누를 식 원 그리기
    if event == cv2.EVENT_RBUTTONDOWN:
        cv2.circle(img, (x, y),50, (0,0,0), thickness = 1)
        cv2.imshow('img', img)
        
    # shift가 눌린 상태에서 마우스 클릭한 좌표를 저장
    if flags & cv2.EVENT_FLAG_SHIFTKEY:
        if event == cv2.EVENT_LBUTTONDOWN:
            pt = (x, y)
            pt_list.append(pt)
            print(pt_list)
            
    elif event == cv2.EVENT_LBUTTONDOWN:
        if pt_list == None:
            print('출력할 좌표가 없거나 하나밖에 없습니다')
        else:
            print(pt_list)
            pt_list_numpy = np.array(pt_list)
            cv2.polylines(img, [pt_list_numpy], isClosed = True, color = (0,0,0), thickness=1)
            pt_list_numpy = []
            pt_list = []
            cv2.imshow('img', img)

   
img = np.ones((512,512,3), np.uint8)+254
cv2.namedWindow('img')
cv2.setMouseCallback('img', mouse_callback, [img])
cv2.imshow('img', img)
key = cv2.waitKey()
if key == 13:
    cv2.imwrite("C:/Users/SBA/opencvDojang/assignment(09-09)/polyline.jpg", img)
    
    src = cv2.imread('C:/Users/SBA/opencvDojang/assignment(09-09)/polyline.jpg')

    if src is None:
        sys.exit('image load failed')
    
    dst1 = cv2.resize(src,(0,0) , fx=0.3, fy=0.3, interpolation = cv2.INTER_AREA)
    dst2 = cv2.resize(src,(0,0) , fx=0.3, fy=0.3, interpolation = cv2.INTER_LINEAR)
    cv2.imshow('src', src)
     
    cv2.imshow('dst1', dst1)
    cv2.imshow('dst2', dst2)
    
    cv2.waitKey()
    cv2.destroyAllWindows()
    
if key == 27:
    cv2.destroyAllWindows()


        
    

            
            
        
