import numpy as np
import cv2
import matplotlib as plt

# Reading an image
img =  cv2.imread('a.png',cv2.IMREAD_GRAYSCALE)
# cv2.IMREAD_COLOR 1
# cv2.IMREAD_UNCHANGED -1


# Show an Image 
cv2.imshow('image',img)


 # Wait for a key to be pressed in milliseconds, if sgiven as <=0 then wait forever
cv2.waitKey(0)

#Close all Windows
cv2.destroyAllWindows()

#plt.imshow(img, cmap='gray', interpolation='bicubic')
