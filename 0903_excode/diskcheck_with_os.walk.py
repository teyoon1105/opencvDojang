# 블랙박스 영상을 저장하는 폴더의 용량을 체크하기 위한 코드

# 특정 디스크의 용량을 계산하는 함수 만들기

import os 



# 특정 폴더의 경로를 입력받음
def get_folder_size(folder_path):
    total_size = 0
    if os.path.exists(folder_path):
        # 특정 폴더 디렉토리 안의 경로, 하위 디렉토리 경로, 파일의 정보를
        # os.walk를 사용하여 가져온다
        for dirpath, dirnames, filenames in os.walk(folder_path):
            # 특정 파일의 이름을 통해
            # 특정 파일의 경로를 추가한다
            for f in filenames:
                fp = os.path.join(dirpath,f)
                # 만약 for를 통해 가져온 filenames의 파일이 심볼릭 파일(다른 파일을 불러오는 링크) 일 경우
                # for문이 무한 루프에 빠질 수 있기 때문에
                # 심볼릭 파일은 if문을 통해 예외 처리를 해준다
                if not os.path.islink(fp):
                    # 심볼릭 파일이 아니면 그 파일의 용량을 total_size 변수값에 저장
                    total_size += os.path.getsize(fp)
                    
    # 만약 해당 폴더가 없는 경우
    # 예외 처리를 해준다
    else:
        print('Error : Folder not found: {}'.format(folder_path))
        
    return total_size

# 폴더 경로 설정
folder_path = "C:/Users/SBA/opencvDojang/data"

# 폴더 용량 계산
total_size_byte = get_folder_size(folder_path)

# 예외처리 밑 단위확인
if total_size_byte == 0:
    print("폴더가 비어 있거나 오류가 발생")
    
else:
    total_size_kb = total_size_byte / 1024
    total_size_mb = total_size_kb / 1024
    total_size_gb = total_size_mb / 1024

    print(total_size_byte) # 기본적으로 byte 단위
    print(total_size_kb) # 1024로 나눠서 kilo byte 단위
    print(total_size_mb) # 1024^2로 나눠서 mega byte 단위
    print(total_size_gb) # 1024^3 으로 나워서 giga byte 단위