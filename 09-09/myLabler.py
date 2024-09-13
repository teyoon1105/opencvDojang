import cv2, sys
import numpy as np
import os
from glob import glob

# data 폴더에서 파일 목록 읽기 > 리스트로 뽑아내기
# 이미지 불러오기
# 마우스 콜백 함수 생성
# 콜백함수 안에서 박스를 그리고, 박스 좌표를 뽑아낸다. (마우스 좌표 2개)
# 참고 : YOLO에서는 박스의 중심좌표(x,y), w, h 사용
# 이미지 파일명과 동일한 파일명으로 txt 파일을 생성
# 추가 : 화살표(>)를 누르면 다음 이미지 로딩됨
# 추가 : 화살표(<)를 누르면 txt 파일이 있다면 박스를 이미지 위에 띄워주기
# 추가 : 박스를 잘못쳤을 때 c(clear)를 누르면 현재 박스 초기화


# 파일을 불러오기 위한 함수
def getImageList():
    # os.getcwd를 사용함
    # cwd : current working dirctory
    # 현재 작업중인 디렉토리, 나같은 경우 Users/SBA/OpenDojang 까지 경로를 가져온다
    basePath = os.getcwd()
    # data를 불러오기 위한 데이터 경로를 위의 경로에 텍스트 연산을 이용해 저장
    dataPath = os.path.join(basePath, 'images')
    # glob을 이용해 위의 dataPath 경로 안에서 .jpg로 끝나는 모든 파일을 filaNames에 저장
    # 리스트로 저장한다
    fileNames = glob(os.path.join(dataPath, '*.jpg'))

    # 해당 리스트를 반환한다
    return fileNames

# 입력받은 이미지와 좌표를 토대로 사작형을 그리는 함수
def drawROI(image, corners):  
    # 그림을 사진 위에 그려 출력하기 위해서는 복사본이 필요
    cpy = img.copy()

    # 입력 받은 좌표값을 출력(제대로 출력이 되었는지 확인)
    print(corners)
    
    # 해당 좌표값을 받아와 좌표값을 사용하여 직사각형을 cpy위에 그린다
    cv2.rectangle(cpy, corners[0], corners[1], color = (128,128,256), thickness = 2)
    
    # 직사각형이 그려진 cpy 파일과 img파일을 addWighted 함수를 통해 합친다
    disp = cv2.addWeighted(img, 0.3, cpy, 0.7,0)
    
    # 합쳐진 파일을 disp로 저장하고 저장한 값을 반환
    return disp


# 마우스 콜백 함수, 콜백이 되는 순간 마우스의 입력에 따라 작동한다
def on_mouse(event, x, y, flags, param):
    global startPt, img, ptList, cpy, textWrData
    
    # 마우스 왼쪽버튼이 눌리면
    if event == cv2.EVENT_LBUTTONDOWN: # 눌리는 딱 한 순간만 이벤트
        # 눌린 마우스 포인터의 좌표값을 startPt값에 저장한다
        startPt=(x,y)
    
    # 마우스 왼쪽버튼이 떼어지면
    elif event == cv2.EVENT_LBUTTONUP: # 
        # ptList에 (떼어지려면 눌려야 하므로 startPt값이 있을테니) startPt와
        # 떼어질 때 마우스 포인터의 좌표를 리스트로 저장
        ptList = [startPt, (x,y)]
        # 파일 생성, 쓰기가 잘 실행되는 지 보기 위한 코드
        textWrData = str(ptList)
        # 마우스를 눌렀다(좌표저장) 때어(좌표저장)  저장된 두 좌표를 토대로
        # drawROI 함수에 입력하여 사각형을 그리고
        # 그려서 나온 사진을 cpy값으로 저장
        cpy = drawROI(img, ptList) 
        # startPt값을 초기화, 전역변수이기 때문
        # ptList를 초기화 하면 더 편하지 않을까?
        ptList = []
        startPt = None
        # label 창 위에 사각형이 그려진 cpy 사진을 올린다
        cv2.imshow('label', cpy) 
    
    # 마우스가 움직이면
    elif event == cv2.EVENT_MOUSEMOVE:
        # 근데? startPt 값이 존재하면? > 즉 왼쪽 버튼이 눌린채 움직인다면
        if startPt:
            # ptList에 startPt와 현재 좌표를 저장
            ptList=[startPt, (x,y)]
            # 계속 사각형을 그려 > 가이드 라인처럼 사용
            cpy = drawROI(img, ptList)
            cv2.imshow('label', cpy)
            
        
        
# main함수
ptList = [] 
startPt = None
cpy=[]
textWrData = None  
    
# fileNames에 원하는 파일(리스트) 가져오기    
fileNames = getImageList()
# 리스트 0번째 사진을 저장
img = cv2.imread(fileNames[0])
# 저장된 파일의 확장자를 txt로 바꿔주기 위해 splitext 사용
filename, ext = os.path.splitext(fileNames[0])

# label 창 생성
cv2.namedWindow('label')
# 마우스 콜백함수, 이제부터 label 창 위에서 마우스의 입력에 반응한다
cv2.setMouseCallback('label', on_mouse, [img])
# label 창을 띄운다
cv2.imshow('label', img)

# 파일을 여러개 처리하기 위해 while문 사용
while True:
    # key값이 들어오기 전까지 무한 대기
    key = cv2.waitKey()
    
    # key값이 들어왔는데, 그 값이 esc면?
    if key == 27:
        # while문 종료
        break
    # key값이 들어왔는데, 그 값이 엔터면?
    elif key == 13:
        # 파일 이름은 txt로 바꾸고
        txtfileName = filename + '.txt'
        # 파일을 w 모드로 열기에 없는 파일이면 생성, 있는 파일이면 덮어쓰기
        f=open(txtfileName,'w')
        # textWrData 값을 저장
        f.write(textWrData)
        #닫는다
        f.close
        # print('before write txt : {}'.format(textWrData))
        
   
# while문을 벗어나면 모든 창을 닫는다.
cv2.destroyAllWindows()