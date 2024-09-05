# 이미지를 4장 불러오기
# 4장의 이미지를 subplot에 한번에 띄우기

# cv2, sys, matplotlib 패키지 가져오기
import cv2, sys
from matplotlib import pyplot as plt

# 이미지 불러오기
imgBGR1 = cv2.imread('data/lena.jpg')
imgBGR2 = cv2.imread('data/apple.jpg')
imgBGR3 = cv2.imread('data/orange.jpg')
imgBGR4 = cv2.imread('data/baboon.jpg')

# 예외처리
if imgBGR1 is None or imgBGR2 is None \
    or imgBGR3 is None or imgBGR4 is None:
    sys.exit('image load failed')
    
# 컬러채널 맞춰주기
imgBGR1 = cv2.cvtColor(imgBGR1, cv2.COLOR_BGRA2RGB)
imgBGR2 = cv2.cvtColor(imgBGR2, cv2.COLOR_BGRA2RGB)
imgBGR3 = cv2.cvtColor(imgBGR3, cv2.COLOR_BGRA2RGB)
imgBGR4 = cv2.cvtColor(imgBGR4, cv2.COLOR_BGRA2RGB)

# matplotlib plt.subplots을 생성하는데
# 생성하는 창의 크기를 figsize로 정한다
# 서브플롯의 축을 전부 없애주고
figsize=(10,10)
fig, ax =plt.subplots(2,2, figsize = figsize)
ax[0][0].axis('off')
ax[0][1].axis('off')
ax[1][0].axis('off')
ax[1][1].axis('off')

# 행렬을 통해 각 서브플롯에 들어갈 파일을 선정
# 추가로 imshow 인수로 aspect = 'auto'로 비율변경 가능
ax[0][0].imshow(imgBGR1)
ax[0][1].imshow(imgBGR2)
ax[1][0].imshow(imgBGR4)
ax[1][1].imshow(imgBGR3)

# matplotlib에서 창 이름 변경 방법
# canvas.manager함수를 통해 생성
fig.canvas.manager.set_window_title('sample window')

# 창 안에 가장 윗부분에 이름 추가
fig.suptitle('image')
plt.show()