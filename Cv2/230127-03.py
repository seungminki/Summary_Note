import cv2
import numpy as np

img = cv2.imread('images/husky.bmp')

kernel = np.array([[1/9, 1/9, 1/9],
                    [1/9, 1/9, 1/9],
                    [1/9, 1/9, 1/9]])

'''
dst = np.zeros(src.shape, dtype=src.dtype)
zeros는 0으로 가득 찬 array를 생성합니다
np.zeros(shape=(10,), dtype=np.int8)
-- 출력 -- 
array([0, 0, 0, 0, 0, 0, 0, 0, 0, 0], dtype=int8)

ones는 zeros와 마찬가지로 1로 가득찬 array를 생성합니다.
np.ones(shape=(10,), dtype=np.int8)

-- 출력 -- 
array([1, 1, 1, 1, 1, 1, 1, 1, 1, 1], dtype=int8)
'''

print(img.shape[:2], img.dtype)
kernel1 = np.ones((3, 3), dtype=img.dtype) / 9
kernel2 = np.ones((3, 3), dtype=np.float64) / 9.
print(kernel1, kernel2)

ke1 = cv2.filter2D(img, -1, kernel1) # 화질이 흐려짐...
ke2 = cv2.filter2D(img, -1, kernel2)
dst2 = cv2.blur(img, (3, 3))
dst3 = cv2.blur(img, (5, 5))
dst4 = cv2.blur(img, (7, 7))

gablur = cv2.GaussianBlur(img, (0, 0), 2)
# 백색 노이즈를 제거하는 데 효과적

cv2.imshow('images', img)
cv2.imshow('kernel1', ke1)
cv2.imshow('kernel2', ke2)
cv2.imshow('blur3', dst2)
cv2.imshow('blur5', dst3)
cv2.imshow('blur7', dst4)
cv2.imshow('GaussianBlur', gablur)
cv2.waitKey()
cv2.destroyAllWindows()