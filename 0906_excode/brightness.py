import cv2
import numpy as np

isColor = True

if not isColor:
    # grayscale

    src = cv2.imread('data/cat.jpg', cv2.IMREAD_GRAYSCALE)
    # print(src.shape)
    # 밝기 변화
    # 모든 픽셀의 밝기 100 증가
    # 밝아짐을 확인 가능
    dst1 = cv2.add(src, 100)
    # cv2 패키지는 영상처리이기 때문에
    # 밝기 255가 넘어가는 add 연산은 255로 saturation이 됨

    # cv2를 사용하지 않고 더하면 255가 넘어가는 픽셀은 다시 0부터 시작하게 되어 오히려 밝기가 어두워짐
    # dst1 = src + 100

    # 이럴때는 범위를 조정
    # dst1 = np.clip(src+100,0,255).astype(np.uint8)
    cv2.imshow('dst1', dst1)
    cv2.imshow('img', src)
    cv2.waitKey()
    cv2.destroyAllWindows()
        
if isColor:
    src= cv2.imread('data/cat.jpg')
    # 색상은 b, g, r 각각 100씩 더해준다
    dst1 = cv2.add(src, (100, 100, 100))
    # dst2= np.clip(src+100, 0, 255).astype(np.uint8)
    
   
    cv2.imshow('img', src)
    cv2.imshow('dst1', dst1)
    cv2.waitKey()
    cv2.destroyAllWindows()