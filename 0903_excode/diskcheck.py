import os

def get_folder_size(folder_path):
    """
    특정 폴더의 용량을 계산하는 함수

    Args:
        folder_path (str): 용량을 확인할 폴더의 경로

    Returns:
        int: 폴더 용량 (바이트)
              폴더가 존재하지 않으면 0 반환
    """

    total_size = 0
    if os.path.exists(folder_path):
        for dirpath, dirnames, filenames in os.walk(folder_path):
            for f in filenames:
                fp = os.path.join(dirpath, f)
                # os.path.islink() 함수를 사용하여 심볼릭 링크는 크기에 포함하지 않도록 함
                if not os.path.islink(fp):
                    total_size += os.path.getsize(fp)
    else:
        print(f"Error: Folder not found: {folder_path}")

    return total_size

# 폴더 경로 설정
folder_path = "C:/Users/SBA/opencvDojang/data"  # 확인하려는 폴더 경로로 변경

# 폴더 용량 계산
total_size_bytes = get_folder_size(folder_path)

# 바이트를 KB, MB, GB로 변환하여 출력
if total_size_bytes == 0:
    print("폴더가 비어 있거나 오류가 발생했습니다.")
else:
    total_size_kb = total_size_bytes / 1024
    total_size_mb = total_size_kb / 1024
    total_size_gb = total_size_mb / 1024

    print(f"폴더 용량 (바이트): {total_size_bytes} 바이트")
    print(f"폴더 용량 (KB): {total_size_kb:.2f} KB")
    print(f"폴더 용량 (MB): {total_size_mb:.2f} MB")
    print(f"폴더 용량 (GB): {total_size_gb:.2f} GB")