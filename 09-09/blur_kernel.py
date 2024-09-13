import cv2, sys
import numpy as np

src = cv2.imread('data2/rose.bmp', cv2.IMREAD_GRAYSCALE)

if src is None:
    sys.exit('image load failed')
    
# 사용자 커널(=필터)를 생성해서 blur 처리
# kernel = np.ones((3,3), dtpye=np.float32)/9
# emboss filter
kernel= np.array([[-2,-1,0],[-1,1,1],[0,1,2]])
dst = cv2.filter2D(src, -1, kernel)


# blur kernel을 사용해서 blur 처리
dst2 = cv2.blur(src,(3,3))

cv2.imshow('img', src)
cv2.imshow('dst', dst)
cv2.imshow('dst2', dst2)
cv2.waitKey()
cv2.destroyAllWindows()