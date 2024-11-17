import qrcode
from PIL import Image

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
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    img.save(qr_filepath)
    print(f"QR code created successfully at {qr_filepath}")


# 사용 예시:
txt_file_path = 'qr_code_create/my_text.txt'  # 텍스트 파일 경로를 여기에 입력하세요.
qr_code_path = 'qr_code_create/my_qr_code.png' # 생성될 QR 코드 파일 경로

create_qr_from_txt(txt_file_path, qr_code_path)