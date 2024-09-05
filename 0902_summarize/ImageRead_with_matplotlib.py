# cv2 패키지와 matplotlib 패키지의 동일한 점
# cv2 패키지와 matplotlib 패키지의 차이점

# 먼저 cv2, sys, matplotlib 패키지 불러오기
import cv2, sys
from matplotlib import pyplot as plt

# 파일주소 저장
fileName = 'data/cat.jpg'

# cv2, matplotlib 패키지의 동일한 점은
# 파일을 불러오는 과정은 같다는 점이다

# 파일경로를 imread 함수를 이용해 불러온다
img = cv2.imread(fileName)

# 제대로 가져오지 못했을 경우를 대비해 예외처리를 한다.
if img is None:
    sys.exit('image load failed')
    
# cv2패키지와 matplotlib의 차이점을 불러온 파일을 창으로 띄울 때이다
# cv2 패키지는 color 채널이 Blue > Green > Red 순으로 채널링이 되어있다
# matplotlib 패키지는 color 채널이 Red > Green > Blue 순으로 채널링이 되어있다
# 때문에 cv2 패키지로 불러온 이미지를 matplolib패키지를 이용해 창으로 출력하면
# Red로 불러와야 할 부분은 Blue로
# Blue로 불러와야 할 부분은 Red로 출력이 되어 색감이 엉망이 된다.
# 때문에 matplotlib을 통해 창으로 출력하려면 color 채널을 변화시켜줘야 한다

# cv2.cvt.Color를 통해 BRG순을 RGB로 바꾼다
imgRGB = cv2.cvtColor(img, cv2.COLOR_BRG2RGB)

# plt를 통해 창으로 출력
plt.imshow(imgRGB) # 창에 imgRGB 파일값을 출력한다
plt.axis('off') # plt을 통해 출력하면 축이 생기는데 이를 없애주는 역할을 한다
plt.show() # 창을 띄운다

# plt을 이용한 창은 cv2와 다르게 창닫기를 사용하여 창을 닫아야 한다.