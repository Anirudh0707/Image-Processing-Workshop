import cv2
import numpy as np

# 500 x 250
img1 = cv2.imread('1.png', 1)
img2 = cv2.imread('2.png', 1)

print(img1.dtype)

add = img1 + img2                               #  255 + 2 = 1          Modulo         257%256

add2 = cv2.add(img1, img2)                      #  255 + 2 = 255         Saturation

add3 = cv2.addWeighted(img1,0.4,img2,0.6,0)         # Here add3 = a*img1 + b*img2 + c      Here a = 0.4; b = 1-a = 0.6 and c=0


cv2.imshow('add1', add)
cv2.imshow('add2', add2)
cv2.waitKey(0)
cv2.destroyAllWindows()
