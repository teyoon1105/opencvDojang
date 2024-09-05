# matplotlib를 사용한 이미지 출력에서 색상을 지정할 때 사용하는 cmap
# matplotlib를 사용한 이미지 출력에서 창의 크기를 조절할 때 픽셀값을 조정하는 interpolation 옵션

# cv2, sys, matplotlib 불러오기
import cv2, sys
from matplotlib import pyplot as plt

# 파일 경로 저장
fileName = 'data/cat.jpg'

# 파일 경로를 통해 파일을 불러오는데, 해당 파일을 밝기 정보만 사용한 흑백으로 가져옴
imgGray = cv2.imread(fileName, cv2.IMREAD_GRAYSCALE)
if imgGray is None:
    sys.exit('image load failed')
    
# plt로 불러오기 때문에 축 없애기
plt.axis('off')
# 다만 cv2.IMREAD_GRAYSCALE로만 불러오면 인식하지 못하기 때문에
# cmap을 이용하여 색상을 인식시켜줘야 한다
# cmap의 디폴트는 color이기 때문에 흑백으로 바꿀 일이 없다면 생략해도 상관없다

# interpolation의 디폴트값은 안티얼라이싱이다, bicubic처럼 조정을 통해 바꿀 수 있다.
plt.imshow(imgGray, cmap='gray', interpolation = 'bicubic' )
plt.show

