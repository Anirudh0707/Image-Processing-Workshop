import cv2
import numpy as np

image = cv2.imread('img.bmp', 1)

eyes = cv2.imread('eyes.bmp', 1)

h , w ,_= eyes.shape

result = cv2.matchTemplate(image, eyes, cv2.TM_CCOEFF_NORMED)

threshold = 0.9
location = np.where( result > threshold )

for pt in zip(*location[::-1]):
    cv2.rectangle(image, pt , ( pt[0]+w , pt[1]+h ), (0,0,0), 10)

cv2.imshow('Image', image)
cv2.waitKey(0)
cv2.destroyAllWindows()