# 파일을 생성 후 가장 오래된 파일을 찾기위해
# 파일의 이름에 따라 정렬을 한다(시간을 기준으로 파일명을 설정했기 때문에)
# 다만 파일명은 str형식이기 때문에
# 0,1,10,11,12,13 이런식으로 정렬을 하기 때문에
# lambda 함수를 사용하여 20240904 부분과 1부분을 나눠 _가 포함되지 않게 하고, int로
# 명시적인 형변환을 한다
# 그 이후 sorted함수를 활용하여 정렬

import os
folderName = os.listdir('test')
sorted_numbers = sorted(folderName, key=lambda x: tuple(map(int, x.split('_'))))

# 추가로 만약 파일을 삭제하고 싶다면
# import os를 한 후
os.system("rmdir /s /q ex1")
# system 함수를 사용하여 윈도우터미널 명령어를 사용하여 삭제할 수 있다
