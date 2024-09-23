import cv2, sys
import numpy as np
import os
import shutil
from glob import glob
from enum import Enum



class funcNum(Enum):
    resize = 1
    rotate = 2
    hflip  = 3
    vflip  = 4
    crop   = 5

class DataAug:
    def __init__(self, dataPath):
        self.dataPath = dataPath
        self.img = None
        self.imageName = None
        self.splitName = None
    
    def getFileList(self, dataPath):
        fileNames = glob(dataPath+'/*.jpg')
        return fileNames
    
    def readImg(self, image_path):
        self.img = cv2.imread(image_path)
        self.imageName = os.path.basename(image_path)
        self.splitName = os.path.splitext(self.imageName)[0]
        return self.img
            
    def dispImg(self):
        return self.img
    
    def resize(self,img=None,dsize=(224,224)):
        if img is None:
            dst = cv2.resize(self.img, dsize, interpolation=cv2.INTER_AREA)
        else:
            dst = cv2.resize(img, dsize, interpolation=cv2.INTER_AREA)
        
        savefileName = self.genFileName(funcNum.resize, 224)
        cv2.imwrite(savefileName,dst)
        return dst
            
    def rotate(self, img=None, multi=True, interAngle=20):
        h, w = img.shape[:2]
        # 튜플로 centerPt를 저장
        centerPt = (w/2, h/2)
        if multi:
            for angle in range(interAngle,360,interAngle):
                # getRotationMatrix2D가 알아서 변환행렬 만들어줌
                aff = cv2.getRotationMatrix2D(centerPt, angle, 1)
                dst = cv2.warpAffine(img, aff, (w, h))
                savefileName = self.genFileName(funcNum.rotate,angle)
                cv2.imwrite(savefileName,dst)
        else:
            aff = cv2.getRotationMatrix2D(centerPt, interAngle, 1)
            dst = cv2.warpAffine(img, aff, (w, h))
            savefileName = self.genFileName(funcNum.rotate,angle)
            cv2.imwrite(savefileName,dst)
            return dst
    
    def flip(self, img=None, hflip=True):
        if hflip:
            if img is None:
                dst = cv2.flip(self.img, 1)
            else:
                dst = cv2.flip(img, 1)
            savefileName = self.genFileName(funcNum.hflip)
            cv2.imwrite(savefileName,dst)            
        else:
            if hflip:
                dst = cv2.flip(img, 1)
            else:
                dst = cv2.flip(img, 0)
                
            savefileName = self.genFileName(funcNum.vflip)
            cv2.imwrite(savefileName,dst)
        return dst               

    def createClassFolder(self, classNames, exist_ok=False):
        for Name in classNames:
            classPath = os.path.join(dataPath, Name)
            
            if not exist_ok:
                shutil.rmtree(classPath)
            
            # 클래스별 폴더를 생성한다.
            os.makedirs(classPath,exist_ok=exist_ok)

    def genFileName(self,procName,value=None):
        if procName==funcNum.resize:
            fileName = self.splitName + '_resize_' + str(value) +'.jpg'
            className = self.splitName.split('_')[0]
            saveName = os.path.join(self.dataPath,className,fileName)
            return saveName
        elif procName==funcNum.rotate:
            fileName = self.splitName + '_rot_' + str(value) +'.jpg'
            className = self.splitName.split('_')[0]
            saveName = os.path.join(self.dataPath,className,fileName)
            return saveName
        elif procName==funcNum.hflip:
            fileName = self.splitName + '_hflip.jpg'
            className = self.splitName.split('_')[0]
            saveName = os.path.join(self.dataPath,className,fileName)
            return saveName
        elif procName==funcNum.vflip:
            fileName = self.splitName + '_vflip.jpg'
            className = self.splitName.split('_')[0]
            saveName = os.path.join(self.dataPath,className,fileName)
            return saveName             


# 전역 변수
DEBUG = True

if __name__ == "__main__":

    # 현재 작업 폴더 기준 데이터 경로 설정
    dataPath = os.path.join(os.getcwd(), 'DataAug')
    # 원본 이미지 경로
    dataOrg = os.path.join(dataPath, 'org')
    # 클래스명은 아래와 같이 4개
    classNames = ['carKey', 'whitePen', 'blackPen', 'airPod']

    # 클래스 객체를 생성
    dataAug = DataAug(dataPath)
    # 클래스별 데이터 증식 폴더를 생성한다.
    exist_ok=False
    dataAug.createClassFolder(classNames,exist_ok)
    fileNames = dataAug.getFileList(dataOrg)

    # if DEBUG:
    #     for fileName in fileNames:
    #         print(fileName)
    
    
    inteAngle = 20  # rotate시 angle간격
    multi=True # rotate시 여러 장을 동시에 실행할지
    
    for fileName in fileNames:
        img = dataAug.readImg(fileName)
        img_resize = dataAug.resize()

        dataAug.rotate(img_resize, multi, inteAngle)
        dataAug.flip(img_resize,hflip=True)
        dataAug.flip(img_resize,hflip=False)