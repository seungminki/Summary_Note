import cv2
import numpy as np

img = cv2.imread('images/lenna.bmp', cv2.IMREAD_GRAYSCALE)

dx = cv2.Sobel(img, -1, 1, 0, delta=128)
dx1 = cv2.Sobel(img, -1, 1, 0, delta=0)

cv2.imshow('images', img)
cv2.imshow('dx', dx)
cv2.imshow('dx1', dx1)

cv2.waitKey()
cv2.destroyAllWindows()