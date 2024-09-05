# plt.imshow함수에서 interpolation 옵션
# cmap은 이미지가 컬러일 경우 cmap지정을 안해도 컬러로 출력됨
# cmap = 'gray'

import cv2, sys
from matplotlib import pyplot as plt

fileName = 'data/cat.jpg'

imgGray = cv2.imread(fileName, cv2.IMREAD_GRAYSCALE)
print(imgGray.shape)

plt.axis('off')
# cmap으로 색상을 지정해주지 않으면 인식하지 못한다.
plt.imshow(imgGray, cmap='gray', interpolation = 'bicubic')
# interpolation의 디폴트는 안티얼라이싱으로 픽셀을 추가로 채워주는 방식
# 다른 방식을 지정하여 사용할 수 있다.
plt.show()