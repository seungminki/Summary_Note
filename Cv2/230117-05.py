import cv2
import sys
import matplotlib.pyplot as plt
import numpy as np

img1 = cv2.imread('images/salt1.jpeg')
img2 = cv2.imread('images/salt2.jpg')

blr1 = cv2.medianBlur(img1, 3)
blr2 = cv2.medianBlur(img2, 5)

cv2.imshow('images1', img1)
cv2.imshow('images2', img2)
cv2.imshow('blr1', blr1)
cv2.imshow('blr2', blr2)

cv2.waitKey()
cv2.destroyAllWindows()