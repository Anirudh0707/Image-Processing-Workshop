import numpy as np
import cv2


img = cv2.imread('camera.jpg',0)
ret, bin =  cv2.threshold(img,100,255,cv2.THRESH_BINARY)

cv2.THRESH_OTSU
#print('try')
print(ret)


'''
book = cv2.imread('book.png',0)

thresh = cv2.adaptiveThreshold(book,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY,115,1)
'''



cv2.imshow('image',bin)
cv2.waitKey(0)
cv2.destroyAllWindows()
