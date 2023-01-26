import cv2
import matplotlib.pyplot as plt

# src = cv2.imread('lenna.bmp', cv2.IMREAD_GRAYSCALE)
# cv2.imshow('images', src)

# hist = cv2.calcHist([src], [0], None, [256], [0, 256])
# plt.plot(hist)
# plt.show()
# ===


src = cv2.imread('lenna.bmp')
cv2.imshow('images', src)

channels = ['b', 'g', 'r']
bgr_plans = cv2.split(src)

for (p, c) in zip(bgr_plans, channels):

    hist = cv2.calcHist([p], [0], None, [256], [0, 256])
    plt.plot(hist, color = c)
plt.show()