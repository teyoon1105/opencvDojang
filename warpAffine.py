import cv2, sys
import numpy as np
import math


def translate(src, x_move=0, y_move=0):
    # 이미지의 이동 변환
    # 이동 변환 행렬
    h, w = src.shape[:2]
    aff = np.array([[1, 0, x_move], [0,1,y_move]], dtype = np.float32)
    # 변환후에 출력되는 배열의 크기 (입력되는 src이미지의 크기를 그대로 출력)
    dst = cv2.warpAffine(src, aff, (h+y_move,w+x_move))
    
    return dst

def shear(src, x_shear=0, y_shear=0):
    
    if x_shear>0 and y_shear==0:
        aff = np.array([[1,x_shear,0],[0,1,0]], dtype=np.float32)
        h, w = src.shape[:2]
        dst = cv2.warpAffine(src, aff, (w + int(h*x_shear), h))
        
    elif y_shear>0 and x_shear == 0:
        aff = np.array([[1,0,0],[y_shear,1,0]], dtype=np.float32)
        h, w = src.shape[:2]
        dst = cv2.warpAffine(src, aff, (h + int(w*y_shear), h))
    
    return dst

# scale보다 resize함수를 사용하는게 좋다
# 직접 scale 함수를 사용해서 확대를  하면 
# interpolation 함수를 사용하기 어렵다
# resize는 interpolation함수를 사용하기 쉽다
def scale(src, x_scale, y_scale):
    h, w = src.shape[:2]
    aff = np.array([[x_scale,0,0],[0,y_scale,0]],dtype=np.float32)
    dst = cv2.warpAffine(src, aff, (w*x_scale, h*y_scale))

# 축소 : 4개의 픽셀 정보를 하나의 픽셀 정보로 합침
# 가끔 정보가 전부 사라져 선이 사라지는 현상 발생
# 블러 처리를 하여 정보를 분산시키고 축소를 시키면
# 해당 현상을 예방할 수 있다    



def rotate(src,rad):
    # 변환 행렬 만들기
    aff = np.array([[np.cos(rad), np.sin(rad), 0], [-np.sin(rad),np.cos(rad)]], dtype = np.float32)
    dst = cv2.warpAffine(src, aff, (0,0))
    
    return dst 

def rotate2(src, angle=20):
    h, w = src.shape[:2]
    # 튜플로 centerPt를 저장
    centerPt = (w/2, h/2)
    aff = cv2.getRotationMatrix2D(centerPt, angle, 1)
    dst = cv2.warpAffine(src, aff, (w, h))
    
    return dst

src = cv2.imread("C:/Users/SBA/opencvDojang/data2/rose.bmp")

if src is None:
    sys.exit('image load failed')

# 512 x 512 >> 1024 x 1024 gotkdehfh tjfwjd
# 해상도를 설정할 수 있다
# 화질은 적당히 좋으며 실행시간돟 적당히 긺
# dst1 = cv2.resize(src,(0,0), fx=4, fy=4, interpolation=cv2.INTER_CUBIC)
# # 화질이 제일 별로, 실행시간도 제일 짧음
# dst2 = cv2.resize(src,(0,0), fx=4, fy=4, interpolation=cv2.INTER_NEAREST)
# # 화질이 제일 좋음, 실행시간이 좀 긺
# dst3 = cv2.resize(src,(0,0), fx=4, fy=4, interpolation=cv2.INTER_LANCZOS4)
    
# dst = translate(src, 50, 50)
# dst = shear(src, 0.5, 0)
# dst = scale(src, 1.5, 1.5)



# 호도법
angle = 20
rad = angle*math.pi/180
# dst = rotate(src, rad)
dst = rotate2(src, angle)

cv2.imshow('src', src)
# cv2.imshow('CUBIC', dst1)
# cv2.imshow('NEAREST', dst2)
# cv2.imshow('LANCZOS4', dst3)
cv2.imshow('dst', dst)
cv2.waitKey()
cv2.destroyAllWindows()