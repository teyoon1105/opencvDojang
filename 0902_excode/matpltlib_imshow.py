# 이미지 불러오기는 동일
# 이미지 출력하기는 차이가 남
# cv2.imshow() --> plt.imshow()로 바꿈
# opencv의 특성과 matplotlib 패키지의 특성의 차이를 이해

import cv2
import sys
from matplotlib import pyplot as plt
fileName = 'data/cat.jpg'

img = cv2.imread(fileName)

if img is None:
    sys.exit('image load failed')
    
# opencv 모듈은 이미지르 읽어올 때 컬러 스페이스의 순서
# B > G > R

# matplolib  패키지는 이미지를 읽어올 때 컬러 스페이스의 순서
# R > G > B
# 때문에 R를 B로 읽어와서 보여줌 > 창백해보임

# cv2.cvtColor
# 채널 컬러 스페이스를 바꿔주는 함수

imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

plt.imshow(imgRGB) # 창에서 img를 그린다
plt.axis('off')
plt.show() # 창을 띄워서 보여준다
# matplotlib은 무조건 창닫기를 사용하여 윈도우를 꺼야 함
# 대신 다양한 컨트롤을 할 수 있음
