import cv2, sys
from datetime import datetime
import os 
# 새로운 thread 함수를 만들어서
# 
basePath = 'blackbox'
now = datetime.now()
folderName = now.strftime("%Y%m%d_%H%M분")
folderName = os.path.join(basePath, folderName)
os.makedirs(folderName, exist_ok=True)

    