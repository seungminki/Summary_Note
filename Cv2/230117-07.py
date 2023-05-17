import cv2
import numpy as np

src = cv2.imread('images/lenna.bmp', cv2.IMREAD_GRAYSCALE)

'''
dx = np.array([[-1, 0, 1],
                [-1, 0, 1],
                [-1, 0, 1]])

dy = np.array([[-1, -1, -1],
                [0, 0, 0],
                [1, 1, 1]])
# 강조 차이
edge_x = cv2.filter2D(img, -1, dx, delta=128)
edge_y = cv2.filter2D(img, -1, dy, delta=128)

edge_x = cv2.Scharr(img, -1, 1, 0, delta=128)
'''

'''
dx = cv2.Sobel(src, cv2.CV_32F, 1, 0)
dy = cv2.Sobel(src, cv2.CV_32F, 0, 1)

mag = cv2.magnitude(dx, dy)
mag = np.clip(mag, 0, 255).astype(np.uint8)

dst = np.zeros(src.shape[:2], np.uint8)
dst[mag > 120] = 255

cv2.imshow('images', src)
cv2.imshow('mag', mag)
cv2.imshow('dst', dst)

# 오...
'''

cv2.waitKey()
cv2.destroyAllWindows()