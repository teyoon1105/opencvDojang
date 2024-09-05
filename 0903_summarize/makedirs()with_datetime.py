# 코드를 통해 폴더를 만들고
# 폴더 안에 파일을 만든다
# 파일명은 오늘 날짜와 현재 시간을 사용

# 윈도우 터미널 명령어를 사용하기 위해 os 패키지 불러오기
# 현재 시간을 불러오기 위해 datetime 패키지 불러오기

import os
from datetime import datetime

# 현재 이 코드를 작성하고 저장하는 폴더에 'test' 이름의 폴더 생성
basePath = 'test'
# basePath를 조절하여 하위 폴더에 또 다른 폴더를 계속 생성할 수 있음
# makedirs 를 사용하여 현재 폴더에 test 폴더 만들기
# exist_ok=True로 설정하여 해당 폴더가 있으면 아무것도 만들지 않게 한다
os.makedirs(basePath, exist_ok=True)

# 현재 시간을 가져온다
now = datetime.now()

# strftime 함수를 이용하여 년, 월, 일, 시간을 표현하고
# 시간은 따로 분리한다
# 일단 시간은 0시~23시로 시간당 하나씩 생성

for hour in range(24):
    # 기본 이름은 20240904_
    folderName = now.strftime("%Y%m%d_")
    # for문을 이용하여 0,1,2,3시 값을 가져와 text 더하기연산
    folderName = folderName + str(hour)
    # folderName을 활용하는 파일을 basePath 폴더 안에 저장할 수 있게 경로 설정
    folderName = os.path.join(basePath, folderName)
    # 파일 생성
    os.makedirs(folderName, exist_ok=True)
    