import matplotlib.pyplot as plt
import cv2
import sys
import numpy as np



# src = cv2.imread('lena.bmp')
# if src is None:
#     print('Image load failed!')
#     sys.exit()

# # print(src.shape)

# cv2.waitKey()
# cv2.destroyAllWindows()


# x_axis = cv2.flip(src, -1)

# # ===
# cv2.imshow('image', src)
# cv2.imshow('x_axis', x_axis)
# cv2.imshow('y_axis', y_axis)
# cv2.imshow('image', src)
# cv2.imshow('image', src)
# cv2.imshow('image', src)

# ch0 = np.zeros((2, 4), np.uint8) + 10

#===

# # 1. 연산에 사용할 배열 생성
# a = np.uint8([[200, 50]])
# b = np.uint8([[100, 100]])

# # 2. Numpy 배열 직접 연산
# add1 = a + b
# sub1 = a - b
# mult1 = a * b
# div1 = a / b

# # 3. OpenCV API를 이용한 연산
# add2 = cv2.add(a,b)
# sub2 = cv2.subtract(a,b)
# mult2 = cv2.multiply(a,2)
# div2 = cv2.divide(a,3)

# # 4. 각 연산 결과 출력
# print(add1, add1)
# print(sub1, sub2)
# print(mult1, mult2)
# print(div1, div2)

# ===

# src1 = cv2.imread('cat.bmp')
# src2 = cv2.imread('husky.bmp')

# if src1 is None or src2 is None:
#     print('Image load failed!')
#     sys.exit()

# dst1 = src1 + src2 # 255가 넘으면 0으로 돌아감
# dst2 = cv2.add(src1, src2, dtype=cv2.CV_8U) # 255가 넘으면 255로 고정

# plt.figure(figsize=(10,8))
# plt.subplot(221), plt.axis('off'), plt.imshow(src1, 'gray'), plt.title('src1')
# plt.subplot(222), plt.axis('off'), plt.imshow(src2, 'gray'), plt.title('src2')
# plt.subplot(223), plt.axis('off'), plt.imshow(dst1, 'gray'), plt.title('dst1')
# plt.subplot(224), plt.axis('off'), plt.imshow(dst2, 'gray'), plt.title('dst2')
# plt.show()

#===

# src = cv2.imread('lenna.bmp')

# if src is None:
#     print('Image load failed!')
#     sys.exit()

# # mask1 = cv2.imread('images/hole.bmp')
# # print(mask1.shape)
# mask = np.full((512, 512, 3), (255, 255, 255), np.uint8)
# cv2.circle(mask, (280, 260), 150, (0, 0, 0), -1)

# dst1 = src + mask
# plt.subplot(221), plt.axis('off'), plt.imshow(src, 'gray'), plt.title('lenna')
# plt.subplot(222), plt.axis('off'), plt.imshow(mask, 'gray'), plt.title('mask')
# plt.subplot(223), plt.axis('off'), plt.imshow(dst1, 'gray'), plt.title('dst1')
# plt.show()

##===



# src1 = np.zeros((300,300), dtype=cv2.CV_8U)
# src2 = np.zeros((150,150, 3),  dtype=cv2.CV_8U)
# h, w = src1.shape[:2]
# cx, cy = w //2, h//2

# cv2.circle(src1, (cx, cy), 100, 250, -1)
# cv2.rectangle(src2, (0, 0, cx, h), 2)

# dst1 = cv2.bitwise_and(src1, src2)
# dst2 = cv2.bitwise_or(src1, src2)
# dst3 = cv2.bitwise_xor(src1, src2)
# dst4 = cv2.bitwise_not(src1, src2)

# plt.subplot(221), plt.axis('off'), plt.imshow(src1, 'gray'), plt.title('src1')
# plt.subplot(222), plt.axis('off'), plt.imshow(src2, 'gray'), plt.title('src2')
# plt.subplot(223), plt.axis('off'), plt.imshow(dst1, 'gray'), plt.title('dst1')
# plt.subplot(224), plt.axis('off'), plt.imshow(dst2, 'gray'), plt.title('dst2')
# plt.subplot(225), plt.axis('off'), plt.imshow(dst3, 'gray'), plt.title('dst3')
# plt.subplot(226), plt.axis('off'), plt.imshow(dst4, 'gray'), plt.title('dst4')
# plt.show()

#===
# src = cv2.imread('lenna.bmp', cv2.IMREAD_GRAYSCALE)
# dst = cv2.add(src, 100)
# dst2 = src + 100
# cv2.imshow('image1', src)
# cv2.imshow('image2', dst)
# cv2.imshow('image3', dst2)
# cv2.waitKey()
# cv2.destroyAllWindows() # 색이 넘어가서 오히려 어두워짐
# # 그레이스케일로 밝기를 100씩 올림

#===

img1 = cv2.imread('lenna.bmp', cv2.IMREAD_COLOR)
img2 = np.zeros((512, 512, 3), np.uint8)
img3 = cv2.imread('lenna.bmp', cv2.IMREAD_GRAYSCALE)
src = cv2.imread('lenna.bmp', 0)

dst1 = cv2.cvtColor(src, cv2.COLOR_BAYER_BG2BGR)

cv2.imshow('image1', img1)
cv2.imshow('image2', img2)
cv2.imshow('image3', img3)
cv2.imshow('src', src)

cv2.waitKey()
cv2.destroyAllWindows()

# orange = cv2.bitwise_and(hsv, mask=h)
# orange = cv2.cvtColor(orange, cv2.COLOR_HSV2BGR)