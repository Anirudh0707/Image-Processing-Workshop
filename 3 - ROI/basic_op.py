import cv2
import numpy as np
import matplotlib.pyplot as plt

img =  cv2.imread('./Images/img.bmp', 1)


# Selecting a reigon in the image specified by the row and column number.
face = img[240:270,240:370] 

cv2.imshow('image1', img)
cv2.imshow('image2', face)
cv2.waitKey(0)
cv2.destroyAllWindows()
