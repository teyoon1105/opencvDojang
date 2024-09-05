import os
#  특정 폴더 안의 파일들을 전부 보여줌

# 순회할 루트 폴더 경로
folder_path = "C:/Users/SBA/opencvDojang/ex1"

# 현재 디렉토리("./")부터 시작하여 모든 하위 폴더 및 파일 정보 출력
# os.walk()함수를 사용하여 폴더 트리 순회
for dirpath, dirnames, filenames in os.walk(folder_path):
    # 현재 폴더 경로 출력
    print("현재 폴더:", dirpath)

    # 현재 폴더 내의 모든 하위 폴더 출력
    print("하위 폴더:", dirnames)

    # 현재 폴더 내의 모든 파일 출력
    print("파일:", filenames)
    print("-" * 30) 