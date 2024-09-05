import os

# 파이썬 실행 프로세스에서 자식 프로세스 생성
# 자식 프로세스로 cmd 터미널 프로세스를 생성
# 그곳에서 터미널 명령어 rmdir 실행
os.system("rmdir /s /q ex1")