import sys
import cv2
import numpy as np
import os
import glob

# print("hello opencv!", cv2.__version__)

# print(np.arange(10)) # 0 ~ n-1
# print(np.zeros((2,3))) # 0으로 채워진 array
# a = np.ones((3,3))
# print(np.zeros_like(a)) # 크기를 튜플로 명시하지 않고 다른 배열과 같은 크기로 생성, 0으로 세팅 
# print(np.ones((2,3))) # 지정된 튜플 크기로 배열 생성하고 1로 세팅
# b = np.zeros((3,3)) # 크기를


# a = np.arange(12)
# print("a ==========", a)
# b = a.reshape((4,3))
# print("b ==========", b)
# c = a.reshape((2,2,-1))
# print("c ==========", c)
# d = b.flatten()
# print("d ==========", d)
# e = c.ravel()
# print("e ==========", e)

# image = np.zeros((300,400), dtype=np.uint8) # 크기 지정
# cv2.imshow('image', image) # 파일 확장자, 파일명
# cv2.waitKey() # 키 기다리기
# cv2.destroyWindow('image')

# img1 = cv2.imread('HappyFish.jpg')
# img2 = img1 # 전염됨
# img3 = img1.copy() # 카피한 사진은 전염되지 않고

# img1.fill(255)
# cv2.imshow('img1', img1)
# cv2.imshow('img2', img2)
# cv2.imshow('img3', img3)
# cv2.waitKey()
# cv2.destroyAllWindows()

# img1 = cv2.imread('dog_640.jpg', cv2.IMREAD_GRAYSCALE)
# img2 = cv2.imread('dog_640.jpg', cv2.IMREAD_COLOR)

# print(img1.shape)
# print(img2.shape) # 컬러는 뒤에 투명도가 하나 더 생김

# cv2.namedWindow('image', flags=cv2.WINDOW_AUTOSIZE)
# cv2.imshow('image', img1)
# cv2.namedWindow('image1', flags=cv2.WINDOW_NORMAL)
# cv2.imshow('image', img2)

# cv2.moveWindow('image', 0, 0)
# cv2.moveWindow('image1', 200, 300)
# cv2.resizeWindow('image', 320, 220)
# cv2.resizeWindow('image1', 320, 220)

# ===
#0. 이미지 파일 다운로드
# https://wallpaperscraft.com/catalog/nature/1920x1080

# # 1. 이미지 파일 리스트에 추가
# filelist = os.listdir('.//images')
# # for file in filelist:
# #     print(file)
# # imgfile = [os.path.join('.//images', file) for file in filelist]
# img_lists = glob.glob('.\\images\\*.jpg')
# print(img_lists)
# # 2. 전체 화면으로 창 생성
# cv2.namedWindow('image', cv2.WINDOW_NORMAL)
# cv2.setWindowProperty('image', cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
# # cv2.setWindowPro

# # 3. 루프 돌면서 이미지 노출
# cnt = len(img_lists)
# idx = 0
# while True:
#     img = cv2. imread(img_lists[idx])

#     if img is None:
#         print("image load failed")
#         sys.exit()

#     cv2.imshow('image', img)

#     if cv2.waitKey(2000) >= 0: # 키보드 입력해야 꺼짐
#         break

#     idx += 1
#     if idx >= cnt:
#         idx = 0

# cv2.destroyAllWindows()
# ===
# 영상을 흑백 영상으로 불러옵니다.
# img = cv2.imread('dog_640.jpg', cv2.IMREAD_GRAYSCALE)

# # 영상이 불러와졌는지 확인
# if img is None:
#     print('Image load failed!')
#     sys.exit()

# # 윈도우 창 생성
# cv2.namedWindow('image')

# # 영상 출력
# cv2.imshow('image', img)

# # 영상 반전 코드
# while True: # 무한 루프
#     keycode = cv2.waitKey() # 키보드 입력 반환 값 저장
#     if keycode == ord('i') or keycode == ord('I'): # i 또는 I 누르면 영상 반전
#         img = ~img               # 영상 반전, 그레이스케일 영상에만 가능
#         cv2.imshow('image', img) # 반전된 영상 출력
#     elif keycode == 27:          # ESC 누를 시 종료
#         break

# # 모든 창 닫기
# cv2.destroyAllWindows()
# ===
# drawing = True
# def draw(event, x, y, flags, param):

#     if event == cv2.EVENT_LBUTTONDOWN:
#         global oldx, oldy, drawing
#         oldx, oldy = x, y
#         drawing = True
#         # print("L button down")

#     elif event == cv2.EVENT_MOUSEMOVE:
#         # print("{}, {}".format(x, y))
#         if drawing == True:
#             cv2.rectangle(img, (oldx, oldy), (x, y), (0, 255, 0), -1)
    
#     elif event == cv2.EVENT_LBUTTONUP:
#         print("L button up")

# img = np.zeros((512, 512, 3), np.uint8)
# cv2.namedWindow('image')
# cv2.setMouseCallback('image', draw)

# while True:
#     cv2.imshow('image', img)
#     # inputkey == cv2.waitKey()
#     keycode = cv2.waitKey()

#     if keycode == 27: # 27은 esc
#         break

# cv2.destroyAllWindows()

# def on_level_change(pos):
#     value = pos * 16
#     if value > 255:
#         value = 255

#     img[:] = value
#     cv2.imshow('image', img)

# img = np.zeros((480, 640, 3), np.uint8)

# cv2.namedWindow('image', cv2.WINDOW_AUTOSIZE)
# cv2.createTrackbar('R', 'image', 0, 16, on_level_change)
# cv2.createTrackbar('G', 'image', 0, 16, on_level_change)
# cv2.createTrackbar('B', 'image', 0, 16, on_level_change)

# while True:
#     cv2.imshow('image', img)
#     # inputkey == cv2.waitKey()
#     keycode = cv2.waitKey()

#     if keycode == 27: # 27은 esc
#         break

#     r = cv2.getTrackbarPos('R', 'image')
#     g = cv2.getTrackbarPos('G', 'image')
#     b = cv2.getTrackbarPos('B', 'image')

#     img[:] = [r, g, b]

# cv2.destroyAllWindows()
# ===
# opencv를 이용한 태극기 그리기
# 지름 지정
c = 400
# 지름으로 태극기 사이즈 구하기
unit = round(c/24)
half_unit = int(unit/2)
# 지름 / 반지름 구하기

crow = unit * 48
ccol = unit * 72

img = np.full((crow, ccol, 3), (255, 255, 255), np.uint8)
# 큰반원 그리기
cx = int(ccol/2)
cy = int(crow/2)
cr = int(c/2)

cv2.ellipse(img, (cx, cy), (cr, cr), 0, 0, 180, (255, 0, 0), -1, cv2.LINE_AA)
cv2.ellipse(img, (cx, cy), (cr, cr), 0, 0, -180, (0, 0, 255), -1, cv2.LINE_AA)
# 작은 반원 그리기
crr = int(cr/2)

# cv2.ellipse(img, (cx + crr, cy), (crr, crr), 0, 0, -180, (255, 0, 0), -1, cv2.LINE_AA)
# cv2.ellipse(img, (cx - crr, cy), (crr, crr), 0, 0, 180, (0, 0, 255), -1, cv2.LINE_AA)

cv2.circle(img, (cx + crr, cy), crr, (255, 0, 0), -1, cv2.LINE_AA)
cv2.circle(img, (cx - crr, cy), crr, (0, 0, 255), -1, cv2.LINE_AA)

# 건곤감리와 태극기 사이 간격구하기
rect_cir_space = 6 * unit
rect_w = 2 * unit


cv2.imshow('image', img)
cv2.waitKey()
cv2.destroyAllWindows()
