# 1. 로컬에 있는 파일(그림)을 불러온다
# 2. 만약 불러오지 못했다면 종료하도록 설정한다
# 3. 불러온 파일을 창에 띄운다
# 4. 창을 닫는다.

# 먼저 영상(사진, 동영상)을 다룰 패키지를 불러온다
import cv2
import sys # 종료를 할 때 사용할 패키지

# 1. 파일을 불러온다
# data폴더 아래 cat.jpg이름을 가진 파일의 경로를 fileName에 저장
fileName = 'data/cat.jpg' 
# 해당 파일의 경로를 cv2.imread에 입력하여 파일을 가져와 img 변수에 저장
img = cv2.imread(fileName)

# 2. 만약 불러오지 못했다면?, 예외처리를 해준다.
if img is None:
    print('image load failed')
    sys.exit()
    # 혹은 sys.exit('image load failed') 이런식으로 작성해도 됨
    
# 3. 창을 통해 불러온 이미지를 출력한다.
# 먼저 띄울 창의 이름을 정하고, 해당 창의 특성을 조정한다.(크기 등)
cv2.namedWindow('cat', cv2.WINDOW_NOMAL)

# 조정을 마친 창에 해당 파일을 출력
cv2.imshow('cat', img)

# 4. 창을 닫는다
# 열린 창을 특정 행위를 할 때 까지 켠 상태로 유지
loop = True

# loop값이 False로 바뀌기 전까지 while문 반복
while(loop):
    # waitKey()함수를 통해 입력받은 key가 q가 아니면 창을 닫지 않는다.
    if cv2.waitKey() == ord('q'):
        # 만약 입력받은 key값이 q면 'cat'창을 닫는다.
        cv2.destroyWindow('cat')
        # loop를 False값으로 변경시켜 while문을 종료
        loop = False 
        
# 불러온 파일을 압축하여 파일을 저장하는 경우
# cv2.inwrite함수를 사용
# cv2.inwrite(저장할 파일 이름, 저장할 파일, 어느정도 퀄리티로 압출할지(파일 크기에 영향))
# cv2.inwrite('cat1.jpg', img, [cv2.IMWRITE_JEPG_QUALITY, 85])



