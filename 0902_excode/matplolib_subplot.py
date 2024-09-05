# 이미지를 4장을 불러온 뒤
# 그 4장을 하나의 창에 띄운다

import cv2, sys
from matplotlib import pyplot as plt

imgBGR1 = cv2.imread('data/lena.jpg')
imgBGR2 = cv2.imread('data/apple.jpg')
imgBGR3 = cv2.imread('data/orange.jpg')
imgBGR4 = cv2.imread('data/baboon.jpg')
# 불러오기 완료
if imgBGR1 is None or imgBGR2 is None \
    or imgBGR3 is None or imgBGR4 is None:
    sys.exit('image load failed')

# 컬러 채널 동일하게 바꿔주기
imgBGR1 = cv2.cvtColor(imgBGR1, cv2.COLOR_BGRA2RGB)
imgBGR2 = cv2.cvtColor(imgBGR2, cv2.COLOR_BGRA2RGB)
imgBGR3 = cv2.cvtColor(imgBGR3, cv2.COLOR_BGRA2RGB)
imgBGR4 = cv2.cvtColor(imgBGR4, cv2.COLOR_BGRA2RGB)

# matplotlib plt.subplots로 이미지를 출력
figsize=(10,10)
fig, ax =plt.subplots(2,2, figsize = figsize)
ax[0][0].axis('off')
ax[0][1].axis('off')
ax[1][0].axis('off')
ax[1][1].axis('off')

ax[0][0].imshow(imgBGR1) # aspect = 'auto'로 비율변경 가능
ax[0][1].imshow(imgBGR2)
ax[1][0].imshow(imgBGR4)
ax[1][1].imshow(imgBGR3)

#  창 이름 추가
fig.canvas.manager.set_window_title('sample window')

# 창 안에 가장 윗부분에 이름 추가
fig.suptitle('image')
plt.show()