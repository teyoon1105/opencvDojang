import cv2, sys

img = cv2.imread('data/lena.png')

if img is None:
    sys.exit('err')

cv2.namedWindow('img')
cv2.imshow('img',img)
key = cv2.waitKey   
while True:
    
    if key == 83:
        break
    elif key == 27:
        break
cv2.destroyAllWindows()