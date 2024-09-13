# 배경 : 흰색 책상, 우드 테이블
# 데이터 증식 조건
# 스마트폰으로 사진 촬영 후 이미지 크기를 줄여주자(resize로 224 X 224)
# 아마 사진을 줄이면 선명도 문제 발생 > 대상의 촬영을 어떻게 해야 할 지 확인
# rotate : 회전(10~30도 범위 안에서 어느 정도 각도를 넣어야 인식이 잘되는가
# hflip, vflip : 도움이 되는가?, 넣을 것인가?
# resize, crop : 가능하면 적용해 보자
# 파일명을 다르게 저장, 원본 : jelly.jpg, 배경이 흰 : jelly_back_while.jpg
# 클래스 별로 폴더 생성
# 데이터를 어떻게 넣느냐에 따라 어떻게 동작되는지 1~2줄로 요약


# 만들어야 하는 함수
# 파일 받아오기 함수
# 파일 명 만들고 저장하기 함수
# rotate 함수
# hflip, vflip 함수
# resize 함수는 일단 보류
# crop

# 구성 순서
# 1. 촬영
# 2. 이미지를 컴퓨터로 복사 후 resize로 224X 224로 축소
# 3. 육안으로 확인, 이렇게 사용해도 되는지 판단
# 4. 함수들을 만든다. resize, rotate, hflip, vflip(연습겸), crop
# 원본 파일명을 읽어서 파일명을 생성하는 기능
# 5. 함수를 활용해서 기능 구현(먼저 단일 함수들이 잘 작동하는 지 판단)
# 6. 테스트(경우의 수 전부 돌려보기)
# 7. 데이터셋을 teachable machine 사이트에 올려서 테스트
# 8. 인식이 잘 안되는 케이스를 분석, 케이스 추가

import cv2, sys
import numpy as np
import os 
import random
from glob import glob
data_org = "C:/Users/SBA/opencvDojang/image_assignment/image/org"
data_rotate = "C:/Users/SBA/opencvDojang/image_assignment/image/rotate_image"
data_crop = "C:/Users/SBA/opencvDojang/image_assignment/image/crop_image"
data_bright = "C:/Users/SBA/opencvDojang/image_assignment/image/bright_image"
data_vflip = "C:/Users/SBA/opencvDojang/image_assignment/image/vflip"
data_hflip = "C:/Users/SBA/opencvDojang/image_assignment/image/hflip"

# 파일을 불러오는 함수
def file_path(name):
    file_split = name.split('\\')
    seper_name = file_split[1]
    return seper_name
    
# dataPath = os.path.join(os.getcwd()) + '/image_assignment'


# fileName = os.path.join(data_org, 'ms_keyboard_white.jpg')
fileNames = glob(os.path.join(data_org, '*.jpg'))


def rotate(resize_img, angle=30):
    global rot_num, data_rotate, file_seper
    h, w = resize_img.shape[:2]
    centerPt = (w/2, h/2)
    aff = cv2.getRotationMatrix2D(centerPt, angle, 1)
    dst = cv2.warpAffine(resize_img, aff, (w,h), borderMode=cv2.BORDER_REFLECT) 
    
    if rot_num < 360:
        rot_num += 30
        # 이름을 파일이름에서 짤라내서 사용해야 함
        rotateFilename = data_rotate + '/{}'.format(file_seper) + '_rotate'+'{}'.format(rot_num) + '.jpg'
        cv2.imwrite(rotateFilename, dst)
    elif rot_num == 360:
        rot_num = 30
        pass
    
        
        
    return dst

def cropping(img):
    global cropped_images, crop_num, data_crop 
    height, width = img.shape[:2]
    crop_height, crop_width = 224, 224
    
    x = random.randint(0, width - crop_width)
    y = random.randint(0, height - crop_height)

    dst = img[y:y + crop_height, x:x + crop_width]
    
    if crop_num < 10:
        crop_num += 1
        # 이름을 파일이름에서 짤라내서 사용해야 함
        cropFilename = data_crop + '/{}'.format(file_seper) + '_crop'+'{}'.format(crop_num) + '.jpg'
        print(cropFilename)
        cv2.imwrite(cropFilename, dst)
    else:
        pass
    
    return dst

def brightness(resize_img, add_num):
    global data_bright
    dst = cv2.add(resize_img, (add_num, add_num,add_num))
    
    brightFilename = data_bright + '/{}'.format(file_seper) + '_bright'+'{}'.format(add_num) + '.jpg'
    cv2.imwrite(brightFilename, dst)
    return dst

def vflip(resize_img):
    global data_vflip
    dst = cv2.flip(resize_img, 0)
    vflipFilename = data_vflip + '/{}'.format(file_seper) + '_vflip'+'.jpg'
    cv2.imwrite(vflipFilename, dst)
    return dst

def hflip(resize_img):
    global data_hflip
    dst = cv2.flip(resize_img, 1)
    hflipFilename = data_hflip + '/{}'.format(file_seper) + '_hflip'+'.jpg'
    cv2.imwrite(hflipFilename, dst)
    return dst

# main
cropped_images = []
rot_num = 0
crop_num = 0
i = 0
 
while True:
    img = cv2.imread(fileNames[i])
    if img is None:
        sys.exit('image load failed')

    file_seper = file_path(fileNames[i])

    crop_img = cv2.resize(img, (300,400))
    
    resize_img = cv2.resize(img, (224, 224), interpolation = cv2.INTER_AREA)
    

    cv2.imshow('resize_img', resize_img)
    key = cv2.waitKey()
    

    while True:
        if key == 13:
            dst = rotate(resize_img, 30)
            cpy = dst.copy()
            resize_img = cpy
            cv2.imshow('dst', dst)
            key = cv2.waitKey()
            
        elif key == ord('c'):
            dst = cropping(crop_img)
            cv2.imshow('dst', dst)
            key = cv2.waitKey()
            
        elif key == ord('d'):
            if i < 6:
                i += 1
                break
            elif i >=6:
                i = 0
                break
        elif key == ord('b'):
            dst = brightness(resize_img, 50)
            cv2.imshow('dst', dst)
            key = cv2.waitKey()
            
        elif key == ord('v'):
            dst = vflip(resize_img)
            cv2.imshow('dst', dst)
            key = cv2.waitKey()
            
        elif key == ord('h'):
            dst = hflip(resize_img)
            cv2.imshow('dst', dst)
            key = cv2.waitKey()
            
        elif key == 27:
            break
    
    if key == 27:
        break
cv2.destroyAllWindows()
