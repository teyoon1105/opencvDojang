import cv2, sys
import numpy as np



# 화살표를 누르면 원이 이동되는 어플
width , height = 290, 174

x,y,R = 256, 256, 5

direction = 0

# main
while True:
    
    img = cv2.imread("C:/Users/SBA/opencvDojang/data/miro2.jpg")
    # img = np.zeros((width, height, 3), np.uint8)+255
    # 원을 그린다, img에 , x,y 중심, R 반지름에, 빨간색 선으로, 안을 채워서
    cv2.circle(img, (x,y), R, (0,0,255), -1)
    cv2.imshow('img', img)
    
    key = cv2.waitKeyEx(30)
    
    # 종료 조건
    if key == 27:
        break
    # right key
    elif key == 0x270000:
        direction = 0
        x += 5
    # down key    
    elif key == 0x280000:
        direction = 1
        y += 5
    # left kkey
    elif key == 0x250000:
        direction = 2
        x -= 5
    # up key  
    elif key == 0x260000:
        direction = 3
        y -= 5
    
    # 경게 확인
    
    if x < R:
        x = R
        direction = 0
        
    if x > width-R:
        x = width-R
        direction = 2
        
    if y < R:
        y = R
        direction = 1
    
    if y > height - R:
        y = height - R
        direction = 3
    
        