import cv2, sys
import numpy as np

# 반지름을 전역변수로 빼놓음
radius = 25

# 입력한 영상과 좌표값을 바탕으로
# 영상 속에 원과 직선을 그리는 함수
def drawROI(img, corners):
    # 전역변수 반지름값을 사용
    global radius
    
    # 이미지 위에 원과 직선을 그리기 위해
    # 레이어를 2개 만들어 하나는 직선과 원을 그려서
    # addWeighted 함수를 사용하여 합치기 위한
    # 복사본
    cpy = img.copy()

    # cpy 영상 위에 그릴 원의 색상
    c1 = (192, 192, 255)
    
    # cpy 영상 위에 그릴 직선의 색상
    c2 = (128, 128, 255)
    
    # cpy 영상 위에 그릴 원과 직선의 선 두께
    lineWidth = 2
    
    # 입력으로 받은 좌표(4개)를 for문을 통해 하나하나씩 가져와서
    for pt in corners:
        # 각 좌표에 반지름(전역변수) 정도로 원을 그린다
        cv2.circle(cpy, tuple(pt.astype(int)), radius, c1, -1, cv2.LINE_AA)
        
    # 입력으로 받은 좌표들을 각각 연결하는 직선을 그린다
    cv2.line(cpy,tuple(corners[0].astype(int)), tuple(corners[1].astype(int)), c2, lineWidth, cv2.LINE_AA)
    cv2.line(cpy,tuple(corners[1].astype(int)), tuple(corners[2].astype(int)), c2, lineWidth, cv2.LINE_AA)
    cv2.line(cpy,tuple(corners[2].astype(int)), tuple(corners[3].astype(int)), c2, lineWidth, cv2.LINE_AA)
    cv2.line(cpy,tuple(corners[3].astype(int)), tuple(corners[0].astype(int)), c2, lineWidth, cv2.LINE_AA)
    
    # 입력으로 받은 img와, 원과 직선을 그린 cpy를 addWeight 함수를 통해 합쳐서
    # disp에 넣는다.
    disp = cv2.addWeighted(img,0.3,cpy,0.7,0)
    
    # drawROI 함수를 사용하면 얻는 결과물
    # 원과 직선을 입력한 좌표에 그린 영상과
    # 원본 영상을 합친 영상을 얻게된다
    return disp


# 마우스 콜백 함수
# 
def mouse_callback(event, x, y, flags, param):
    global srcQuad, dragSrc, img2, radius ,ptOld
    
    
    if event == cv2.EVENT_LBUTTONDOWN:
        for i in range(4):
            if cv2.norm(srcQuad[i]-(x,y))<radius:
                dragSrc[i] = True
                
                ptOld = (x,y)
                
                break
    if event == cv2.EVENT_LBUTTONUP:
        for  i in range(4):
           
            dragSrc[i] = False
            
   
    if event == cv2.EVENT_MOUSEMOVE:
        for i in range(4):
            if dragSrc[i]:
                dx = x-ptOld[0]
                dy = y-ptOld[1]

                srcQuad[i] += (dx, dy)
                cpy = drawROI(img2, srcQuad)
                cv2.imshow('cpy', cpy)
                ptOld = (x,y)
                break

# main
# data2에 있는 book 영상을 읽어온다
img = cv2.imread('data2/book.jpg')

# 예외처리
if img is None:
    sys.exit('image load failed')
    
# img 파일은 너무 크기 때문에 resize를 통해 크기를 축소시킨다  
img2 = cv2.resize(img, (0,0), None, fx = 0.5, fy = 0.5)

# 축소시킨 해당 이미지의 너비와 높이를 각각 받아와 w, h에 저장
w,h = img2.shape[1], img2.shape[0]
# print(w,h)



# 원을 그릴 좌표값을 생성
spare =50
srcQuad = np.array([[spare, spare],[w-spare, spare],[w-spare, h-spare], [spare, h-spare]], np.float32)

# 마우스 콜백함수를 사용해서 옮긴 원과 직선으로 구분된 부분을 새로운 창에 띄울 때
# 직사각형의 좌표값
dstQuad = np.array([[0,0],[w-1,0], [w-1, h-1], [0, h-1]], np.float32)

# 원을 클릭해서 드래그를(mousemove) 하는 지 판단하기 위한 boolean값
dragSrc = [False, False, False, False]

# drawROI 함수를 통해 img2와 cpy를 합친다
disp = drawROI(img2, srcQuad)
 
# cpy 창 만들기
cv2.namedWindow('cpy')
# 마우스 콜백함수
cv2.setMouseCallback('cpy', mouse_callback, [img2])
cv2.imshow('cpy',disp)

while True:
    
    key = cv2.waitKey()
    
    if key == 13:
        break
    elif key == 27: 
        cv2.destroyAllWindows()
        sys.exit()
        
# 원본 이미지의 srcQuad의 좌표를 기준으로 원근 변환을 위해 행렬을 생성
pers = cv2.getPerspectiveTransform(srcQuad, dstQuad)
# 원근 행렬을 이용하여 너비 w, 높이 h의 영상 출력
dst = cv2.warpPerspective(img2, pers, (w,h))

cv2.imshow('dst', dst)
cv2.waitKey()
cv2.destroyAllWindows()
