import cv2, sys
import numpy as np
from matplotlib import pyplot as plt

isColor = True

if not isColor:
    src1 = cv2.imread('data2/Hawkes.jpg', cv2.IMREAD_GRAYSCALE)
    src2 = cv2.imread('data2/Hawkes_norm.jpg', cv2.IMREAD_GRAYSCALE)


    if src1 is None or src2 is None:
        sys.exit('image load failed')
        
    # 히스토그램을 만들기
    hist1 = cv2.calcHist([src1], [0], None, [256], [0,256])
    hist2 = cv2.calcHist([src2], [0], None, [256], [0,256])

if isColor:
    src = cv2.imread('data/Lena.bmp')
    
    if src is None:
        sys.exit('image load failed')
    
    # 컬러 채널 분리
    colors = ['b', 'g', 'r']
    bgr_planes = cv2.split(src)
    
    for  (p,c) in zip(bgr_planes, colors):
        hist = cv2.calcHist([p], [0], None, [256], [0, 256])
        plt.plot(hist, color=c)
        
cv2.imshow('Lena', src)
plt.show()
        
        
        
        
        
    # cv2.imshow('src1', src1)
    # # matplotlib 띄우기
    # plt.plot(hist1)
    # plt.plot(hist2)
    # plt.show()
    # cv2.waitKey()
    # cv2.destroyAllWindows()