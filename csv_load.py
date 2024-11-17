import pandas as pd
import os

my_dir = os.getcwd()

# csv파일 경로 설정
csv_path = os.path.join(my_dir, "txt_food.csv")

# 데이터 프레임으로 가져오기
csv_test = pd.read_csv(csv_path)

# 확인
csv_test
