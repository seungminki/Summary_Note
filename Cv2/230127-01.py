import cv2
import sys
import matplotlib.pyplot as plt
import numpy as np

src = cv2.imread('images/road.jpg')
print(src.shape, src.dtype)
dst = np.zeros(src.shape, dtype=src.dtype)

N = 32
# ROI의 평균값으로 이미지 나타내기
# 평균값, N이 커질수록 원본과 비슷해지고 작을 수록 평균값과 비슷해져 구분하기 어려워짐
h, w, _ = src.shape

h = h // N
w = w // N

for i in range(N):
    for j in range(N):
        y = i * h
        x = j * w
        roi = src[y:y+h, x:x+w]
        dst[y:y+h, x:x+w] = cv2.mean(roi)[0:3]


roi = cv2.selectROI(dst)
# Select a ROI and then press SPACE or ENTER button!
# Cancel the selection process by pressing c button!
# enter를 누르면 영역이 선택되고 c를 누르면 취소됨
print('roi = ', roi)

img = dst[roi[1] : roi[1] + roi[3], roi[0] : roi[0] + roi[2]]

cv2.imshow('img', img)

cv2.waitKey()
cv2.destroyAllWindows()
