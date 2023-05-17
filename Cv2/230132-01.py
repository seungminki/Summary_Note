import sys
import numpy as np
import cv2

# src = cv2.imread('images/cells.jpg', cv2.IMREAD_GRAYSCALE)
img_color = cv2.imread('images/test4.jpg')
img_gray = cv2.cvtColor(img_color, cv2.COLOR_BGR2GRAY)

if img_color is None:
    print('Images load failed!')
    sys.exit()

'''
def on_threshold(pos):
    _, dst1 = cv2.threshold(src, pos, 255, cv2.THRESH_BINARY)
    cv2.imshow('dst1', dst1)

cv2.imshow('src', src)
# Trackbar 만들 Window 지정
cv2.namedWindow('dst')
cv2.createTrackbar('threshold', 'dst', 0, 255, on_threshold)
cv2.setTrackbarPos('threshold', 'dst', 128)
'''

'''
_, dst1 = cv2.threshold(src, 100, 255, cv2.THRESH_BINARY)
_, dst2 = cv2.threshold(src, 210, 255, cv2.THRESH_BINARY)

images = [src, dst1, dst2]
merged = np.hstack(images)
cv2.imshow('merged', merged)
# vstack = 세로 결합, hstack = 가로 결합
'''
'''
# 전역 이진화
_, dst = cv2.threshold(src, 230, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)

# 지역 이진화 4*4=16
'''
'''
def on_threshold(pos):
    bsize = pos
    if bsize % 2 == 0:
        bsize -= 1

    if bsize < 3:
        bsize = 3
    dst = cv2.adaptiveThreshold(src, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C
                                , cv2.THRESH_BINARY, pos, 5)
    cv2.imshow('dst', dst)

cv2.imshow('src', src)
cv2.namedWindow('dst')
cv2.createTrackbar('Block', 'dst', 0, 255, on_threshold)
cv2.setTrackbarPos('Block', 'dst', 11)
'''

'''
cv2.adaptiveThreshold(src, maxValue, adaptiveMethod, thresholdType, blockSize, C)
Parameters:
src - graysclae image
maxValue - 임계값
adaptiveMethod - thresholding value를 결정하는 계산 방법(mean, gaussian 방식)
thresholdType - threshold 방법
blockSize - thresholding을 적용할 영역 사이즈, 홀수(3, 5, 7, ...)
C - 계산된 경계값(평균이나 가중평균)에서 차감할 값

AdptiveMethod
Mean 방식은 지정된 영역의 이웃 픽셀의 평균으로 threshold를 결정하는 방법
Gaussian 방식은 가우시안 분포에 따른 가중치의 합으로 threshold를 결정하는 방법
'''

# images = [src, dst]
# merged = np.hstack(images)
# cv2.imshow('merged', merged)
# cv2.waitKey()
# cv2.destroyAllWindows()

'''
import cv2
import matplotlib.pyplot as plt

block_size = 9
C = 5
img = cv2.imread('images/block.jpg', cv2.IMREAD_GRAYSCALE)

ret, th1 = cv2.threshold(img, 0, 255, cv2.THRESH_OTSU)
th2 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, block_size, C)
th3 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, block_size, C)

imgs = {'Original': img, f'Global-Otsu:{ret}': th1,
        'Adapted-Mean':th2, 'Adapted-Gaussian': th3}

for i, (k, v) in enumerate(imgs.items()):
    plt.subplot(2, 2, i+1)
    plt.imshow(v, 'gray')
    plt.title(k)
    plt.xticks([])
    plt.yticks([])
plt.show()
# 위 결과 영상에서 볼 수 있듯이 Otsu 알고리즘은 하나의 값으로 thresholding하는 것으로 
# 영상의 조명이 달라지는 부분은 모두 없어졌다. 하지만 Adaptive Thresholding(Mean, Gaussian)을 적용한 영상은 훨씬 좋은 결과를 보인다.
'''
'''
_, src_bin = cv2.threshold(src, 0, 255, cv2.THRESH_OTSU)

cnt, labels, stats, centroids = cv2.connectedComponentsWithStats(src_bin)
print('cnt1: ', cnt)

dst = cv2.cvtColor(src, cv2.COLOR_GRAY2BGR)

for i in range(1, cnt): # 각각의 객체 정보에 들어가기 위해 반복문. 범위를 1부터 시작한 이유는 배경을 제외
    (x, y, w, h, area) = stats[i]

    # 노이즈 제거
    if area < 20:
        continue

    cv2.rectangle(dst, (x, y, w, h), (0, 255, 255))
'''
'''
ret, img_binary = cv2.threshold(img_gray, 127, 255, 0)
contours, hierarchy = cv2.findContours(img_binary, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)

for cnt in contours:
    cv2.drawContours(img_color, [cnt], 0, (255, 0, 0), 3)


for cnt in contours:
    M = cv2.moments(cnt)

    cx = int(M['m10']/M['m00'])
    cy = int(M['m01']/M['m00'])

    cv2.circle(img_color, (cx, cy), 10, (0, 0, 255), -1)

for cnt in contours:
    x, y, w, h = cv2.boundingRect(cnt)
    cv2.rectangle(img_color, (x, y), (x+w, y+h), (0, 255, 0), 2)

for cnt in contours:

    rect = cv2.minAreaRect(cnt)
    box = cv2.boxPoints(rect)
    box = np.int0(box)
    cv2.drawContours(img_color, [box], 0, (0, 0, 255), 2)

cv2.imshow("result", img_color)
cv2.waitKey(0)
'''
ret, img_binary = cv2.threshold(img_gray, 127, 255, 0)
contours, hierarchy = cv2.findContours(img_binary, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)

for cnt in contours:
    cv2.drawContours(img_color, [cnt], 0, (255, 0, 0), 3)


for cnt in contours:
    epsilon = 0.02 * cv2.arcLength(cnt, True)
    approx = cv2.approxPolyDP(cnt, epsilon, True)
    
    vtc = len(approx)
    print(vtc)

    if vtc == 3:
        pass


    cv2.drawContours(img_color, [approx], 0, (0, 255, 255), 5)

print(len(approx))
print(type(approx))

cv2.imshow("result", img_color)
cv2.waitKey(0)

