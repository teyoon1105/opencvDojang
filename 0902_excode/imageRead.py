# 파일에서 이미지를 읽어서 출력

import cv2
import sys

fileName = 'data/cat.jpg'

# 이미지를 불러오는 함수
img =cv2.imread(fileName)
print(img.shape)
# width, height, channel순

# 예외처리 루틴 : 이미지를 읽어오지 못했을 때
if img is None:
    print('Image load failed')
    #프로그램 종료
    sys.exit()
    
    
# 창에 이미지 출력
# 이름뿐만 아니라 창의 특성도 변화시킬 수 있다
cv2.namedWindow('cat', cv2.WINDOW_NORMAL)
# img창에 img파일을 출력
cv2.imshow('cat', img)

# 이미지 배열을 파일로 저장하는 함수
# cv2.imwrite('cat1.jpg', img, [cv2.IMWRITE_JPEG_QUALITY, 85])
# cv2.imwrite('cat2.jpg', img, [cv2.IMWRITE_JPEG_QUALITY, 95])
# 파일을 저장할 때 영상 화질 조절을 통해 파일의 크기를 조절할 수 있다

loop = True
while(loop):
    if cv2.waitKey() == ord('q'):
    # 모든 창 닫기
        cv2.destroyWindow('cat')
        loop=False
    

