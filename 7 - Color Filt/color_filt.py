import cv2
import numpy as np

img = cv2.imread('a.png',1)

hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)

lower_color = np.array([0,100,100])
upper_color = np.array([10,255,255])

mask = cv2.inRange(hsv, lower_color, upper_color)
out = cv2.bitwise_and(img,img,mask=mask)

cv2.imshow('original',img)
cv2.imshow('output',out)
cv2.waitKey(0)
cv2.destroyAllWindows()