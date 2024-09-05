import os
from datetime import datetime

# 폴더를 생성
# 현재 폴더 아래에 test폴더를 생성
# test폴더 아래에 날짜_시간 폴더를 생성

basePath = 'test'
# 폴더 만드는 함수
# 폴더 속 폴더 속 폴더를 만들 수 있음
os.makedirs(basePath, exist_ok=True)

# 현재 시간 가져오기
now = datetime.now()

# 폴더명 : '20240904_11'
# folderName=now.strftime("%Y%m%d_%H")
# print(folderName)

for hour in range(24):
    folderName = now.strftime("%Y%m%d_")
    folderName = folderName + str(hour)
    folderName = os.path.join(basePath, folderName)
    os.makedirs(folderName, exist_ok=True)
    