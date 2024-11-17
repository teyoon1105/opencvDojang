import qrcode
from PIL import Image
import os 

def create_qr_from_txt(txt_filepath, qr_filepath):
    """
    텍스트 파일의 내용을 QR 코드로 생성합니다.

    Args:
        txt_filepath: 텍스트 파일 경로.
        qr_filepath: 생성될 QR 코드 이미지 파일 경로.
    """
    try:
        with open(txt_filepath, 'r', encoding='utf-8') as f:  # UTF-8 인코딩을 사용하여 유니코드 지원
            data = f.read()
    except FileNotFoundError:
        print(f"Error: File not found at {txt_filepath}")
        return

    # QR 코드 생성 및 저장
    qr = qrcode.QRCode(
        # qr의 구조적 크기 21x21
        version=1,
        # ERROR_CORRECT_L: 약 7%의 오류 정정 (가장 낮은 수준)
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        # qr코드의 시각적 크기
        box_size=10,
        # qr코드 테두리 크기
        border=4,
    )
    # 인코딩 된 데이터를 qr에 추가해줌
    qr.add_data(data)
    # qr코드에 데이터가 저장될 수 있게끔 최적화를 해줌
    qr.make(fit=True)
    # qr코드를 이미지로 생성
    img = qr.make_image(fill_color="black", back_color="white")
    img.save(qr_filepath)
    print(f"QR code created successfully at {qr_filepath}")

my_dir = os.getcwd()

# 사용 예시:
txt_file_path = os.path.join(my_dir + 'my_text.txt')  # 텍스트 파일 경로를 여기에 입력하세요.
qr_code_path =  os.path.join(my_dir + 'my_qr_code.png') # 생성될 QR 코드 파일 경로

create_qr_from_txt(txt_file_path, qr_code_path)