import cv2, sys
import numpy as np
import matplotlib.pyplot as plt
pt1 = (0,0)
pt2 = (0,0)
# 마우스 콜백 함수 구현
# 마우스에서 이벤트가 발생하면서 호출되는 함수
# 버튼, 클릭,마우스 좌표를 이용
def mouse_callback(event, x, y, flags, param):
    img = param[0]
    global pt1, pt2

    # if event == cv2.EVENT_LBUTTONDOWN:
    #     print('lbutton down')
    
    # elif event == cv2.EVENT_LBUTTONUP:
    #     print('lbutton up')
        
    # elif event == cv2.EVENT_MOUSEMOVE:
    #     print('mouse move : x : {}, y : {}'.format(x, y))
    
    # if event == cv2.EVENT_LBUTTONDOWN:
    #     cv2.circle(img, (x,y), 100, (0,0,255), 3)
    # # 그림 화면을 업데이트   
    # cv2.imshow('img', img)
    
    if event == cv2.EVENT_LBUTTONDOWN:
        pt1 = (x, y)
        
    elif event == cv2.EVENT_LBUTTONUP:
        pt2 = (x,y)
        cv2.rectangle(img, pt1, pt2, (255,0,0), 3)
        
    cv2.imshow('img', img)
        
        

    
    

# 흰색 캔버스를 생성
img = np.ones((512,512,3), np.uint8)+254
# 메인에서 setMouceCallback 함수를 실행하면서 콜백함수를 지정
cv2.namedWindow('img')
cv2.setMouseCallback('img', mouse_callback, [img])
cv2.imshow('img', img)
cv2.waitKey()
cv2.destroyAllWindows()