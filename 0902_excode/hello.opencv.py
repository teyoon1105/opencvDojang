import sys
import cv2

print('Hello OpenCV', cv2.__version__)


# image read('파일명')
# 뒤의 파일을 가져와서 img 객체를 생성
# imread로 불러온 객체는 numpy ndarray 데이터형
img_gray = cv2.imread('data/lenna.bmp', cv2.IMREAD_GRAYSCALE)
img_bgr = cv2.imread('data/lenna.bmp')



# 파일을 못찾아서 이미지를 못 읽어온 경우
# 프로그램 종료
if img_gray is None or img_bgr is None:
    print('Image load failed!')
    sys.exit()

# 창의 이름은 image로 정의
cv2.namedWindow('image_gray')
cv2.namedWindow('image_bgr')

# 불러온 이미지를 창에 띄워준다
# 창의 이름은 image

cv2.imshow('image_gray', img_gray)
cv2.imshow('image_bgr', img_bgr) 
# 키입력을 기다리는 함수
# 함수 안에 값을 입력 단위 : ms
# waitkey함수에 자
# 연값을 설정하지 않으면 무한대기
# 키보드의 입력이 들어올 때 까지
cv2.waitKey()

# 모든 창을 다 닫는다.
cv2.destroyAllWindows()