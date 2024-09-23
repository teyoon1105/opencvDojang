# 함수 스타일로 코딩

import cv2, sys
import numpy as np
import os
from glob import glob
import shutil
from enum import Enum

# 클래스에 내장될 기능을 번호로 설정
class func_num(Enum):
    resize = 1
    rotate = 2
    hflip  = 3
    vflip  = 4
    crop   = 5
# 전역변수
DEBUG = True
dsize = (224, 224)
# input  : data_path
# output : data_path 안에 jpg파일의 리스트를 가져오기 
# img_type의 리스트를 추가하여 입력하면, 나중에 data_path안에 있는 jpg 뿐만 아니라 
# jpeg, png, bmp 등의 파일들을 검사하여 원하는 type을 골라낼 수 있다
data_path = "C:/Users/SBA/opencvDojang/image_assignment/image/org"

def getFileList(data_path): 
    fileNames = glob(os.path.join(data_path, '*.jpg'))
    # if DEBUG:
    #     print(fileNames)
    return fileNames

# 이미지 불러오는 함수
def read_img(image_path):
    # if DEBUG:
    #     print(image_path)
    img = cv2.imread(image_path)
    
    if img is None:
        sys.exit('image load failed')
    
    return img  

# input   : 원본 파일명
# output  : 새로 생성될 파일명
def getFileName(imgName, func):
    if func == func_num.resize:
        # 경로만 제외한 파일명만 올려낸다
        baseName = os.path.basename(imgName)
        # 확장자만 분리
        baseNameSplit = os.path.splitext(baseName)[0]
        
        resizeFilename = baseNameSplit + '_resize' + str(dsize[0]) + '.jpg'
        if DEBUG:
            print(resizeFilename)
            
        return resizeFilename

def resize(img=None, dsize=dsize, imgName=None):
    if img is None:
        print('image Path is None')
    
    dst = cv2.resize(img, dsize, interpolation = cv2.INTER_AREA)
    
    # 새로 만들 파일명 가져오기
    resizeName = getFileName(imgName, func_num.resize)
    # 파일 저장 기능까지
    cv2.imwrite(resizeName, dst)
    return dst
    
classList = ['ms_keyboard', 'ty_keyboard', 'yg_keyboard']   
def createFolder():
    for classname in classList:
        # 기존의 폴더가 있으면 삭제하고, 새로 생성
        # 폴더 안에 파일이 존재하더라도, 파일과 폴더를 모두 삭제
        classPath = os.path.join(data_path,classname)
        
        # shutil을 사용한 rmtree 폴더 삭제는 경로를 잘못 선택할 시 모든 파일이 한번에 날라갈 수 있기 때문에
        # 항상 사용하기 전에 print를 사용하여 지정한 경로가 맞는지 판단해야 한다
        if os.path.isdir(classPath):
            # print(classPath)
            shutil.rmtree(classPath)
            
        os.makedirs(classPath,exist_ok=True) 
    


def main():
    createFolder()
    fileNames = getFileList(data_path)
    for fileName in fileNames:
        img = read_img(fileName)
        dst = resize(img, dsize, fileName)
        cv2.imshow('dst', dst)
        cv2.waitKey()
        break
    
    cv2.destroyAllWindows()
    
    
if __name__ == "__main__":
    main()

