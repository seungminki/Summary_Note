
import numpy as np
import matplotlib.pyplot as plt
import cv2
import sys

'''
img = cv2.imread('images/lenna.bmp', cv2.IMREAD_GRAYSCALE)

f = np.fft.fft2(img)
fshift = np.fft.fftshift(f)
# mag = 20*np.log(np.abs(fshift))

h, w = img.shape[0:2]
crow, ccol = (int)(h/2), (int)(w/2)


fshift[crow-30: crow+30, ccol-30:ccol+30] = 0

# 푸리에 이미지화
f_ishift = np.fft.ifftshift(fshift)
img_back = np.fft.ifft2(f_ishift)
img_back = np.abs(img_back)

plt.subplot(121), plt.imshow(img, cmap='gray'), plt.title('input'), plt.axis('off')
# plt.subplot(122), plt.imshow(mag, cmap='gray'), plt.title('magnitude Spectrum'), plt.axis('off')
plt.subplot(121), plt.imshow(img_back, cmap='gray'), plt.title('HPF'), plt.axis('off')
plt.subplot(121), plt.imshow(img_back), plt.title('JET'), plt.axis('off')
plt.show()
'''

'''
# 이미지 위치 변화
src = cv2.imread('images/lenna.bmp')
dx, dy = 200, 150
# dx, dy = 0, 0
# Numpy 배열, 2차원 배열, 2(세로)*3(가로) array
aff = np.array([[1, 0, dx],
                [0, 1, dy]], dtype=np.float32)

dst = cv2.warpAffine(src, aff, (0, 0))
dst2 = cv2.warpAffine(src, aff, (0, 0), None, cv2.INTER_LINEAR, cv2.BORDER_CONSTANT, (255, 0, 0))

cv2.imshow('src', src)
cv2.imshow('dst', dst)
cv2.imshow('dst2', dst2)
cv2.waitKey()
cv2.destroyAllWindows()
'''

'''

# 어파인 행렬 생성
aff = np.array([[1, 0.5, 0],
                [0, 1, 0]], dtype=np.float32)

aff1 = np.array([[0.5, 0, 0],
                [0, 0.5, 0]], dtype=np.float32)

aff2 = np.array([[2, 0, 0],                
                [0, 2, 0]], dtype=np.float32)

h, w = src.shape[:2]

# 영상 크기가 짤리므로 세로(h)는 고정, 가로(w)는 늘리기
dst = cv2.warpAffine(src, aff, (w+int(h*0.5), h))
dst1 = cv2.warpAffine(src, aff1, (w+int(h*0.5), h))
dst2 = cv2.warpAffine(src, aff2, (w+int(h*0.5), h))

'''

'''
# 사진 확대
dst = cv2.resize(src, (0, 0), fx=4, fy=4, interpolation=cv2.INTER_NEAREST)

scale_percent = 60
w = int(src.shape[1]* scale_percent / 100)
h = int(src.shape[0]* scale_percent / 100)
dst1 = cv2.resize(src, (w, h), interpolation=cv2.INTER_CUBIC)

w = 400
h = src.shape[0]
dst2 = cv2.resize(src, (w, h), interpolation=cv2.INTER_AREA)

w = src.shape[1]
h = 200
dst2 = cv2.resize(src, (w, h), interpolation=cv2.INTER_AREA)

dst3 = cv2.resize(src, (1980, 1280), interpolation=cv2.INTER_AREA)

print(src.shape)
'''

'''
# (320, 240, 3)
dst1 = cv2.resize(src, (0, 0), fx=4, fy=4, interpolation=cv2.INTER_NEAREST) # 스케일 팩터 이용
dst2 = cv2.resize(src, (1920, 1280))  # cv2.INTER_LINEAR, 픽셀 크기 지정
dst3 = cv2.resize(src, (1920, 1280), interpolation=cv2.INTER_CUBIC) # 픽셀 크기 지정
dst4 = cv2.resize(src, (1920, 1280), interpolation=cv2.INTER_LANCZOS4) # 픽셀 크기 지정

# NEAREST와 LINEAR의 화질 차이가 큼
# 나머지 보간법은 LINEAR와 큰 차이를 느낄 수 없음
# 따라서 속도도 빠르고 퀄리티도 적당한 LINEAR을 많이 씁니다
cv2.imshow('src', src)
cv2.imshow('dst1', dst1[500:900, 400:800]) # 영상 크기가 너무 커서 일정 부분만 출력
cv2.imshow('dst2', dst2[500:900, 400:800])
cv2.imshow('dst3', dst3[500:900, 400:800])
cv2.imshow('dst4', dst4[500:900, 400:800])
cv2.waitKey()
cv2.destroyAllWindows()

# 영상 축소 시 디테일이 사라지는 경우가 발생합니다
# 한 픽셀로 구성된 성분이 축소를 하게 되면서 사라지는 경우가 발생합니다
# 이를 해결하기 위해 입력 영상을 부드럽게 필터링 한 후 축소를 하거나 여러번 축소를 반복합니다.
# opencv의 cv2.resize 함수에서는 cv2.INTER_AREA 플래그를 사용합니다.
'''


'''
print(src.shape[:2])

rc = (250, 120, 200, 200)
cpy = src.copy()
cv2.rectangle(cpy, rc, (0, 0, 255), 2)
cv2.imshow('src', cpy)

for i in range(1, 4):
    src = cv2.pyrDown(src)
    cpy = src.copy()
    cv2.rectangle(cpy, rc, (0, 0, 255), 2, shift=i)
    filename = 'cat%s.jpg' % i
    cv2.imwrite(filename, src)
    cv2.imshow('src', cpy)
    cv2.waitKey()
    cv2.destroyWindow('src')

cv2.destroyAllWindows()
'''
'''
# 라플라시안 피라미드
# 앞서 가우시안 피라미드로 나온 결과를 보시면 pyUp()으로 이미지를 확대하면 화질이 떨어지는 것을 볼 수 있습니다
# 이러한 문제를 해결하기 위하여 라플라시안 피라미드를 사용합니다
# 라플라시안 피라미드는 가우시안 피라미드의 이미지와 상위 단계(해상도는 낮지만 스케일은 높음)의 이미지를
# 확장시킨 이미지의 차이로 구성됩니다.
# 즉, 가우시안 피라미드로 만들어진 이미지들을 가지고 라플라시안 피라미드를 만든다는 의미
img = cv2.imread('images/lenna.bmp')

# 원본 이미지를 가우시안 피라미드로 축소
Down_img = cv2.pyrDown(img)

# 축소한 이미지를 가우시안 피라미드로 확대
Down_to_Upimg = cv2.pyrUp(Down_img)

# 원본 이미지와 2번으로 처리한 이미지를 뺌
laplacian = cv2.subtract(img, Down_to_Upimg)

# 2번과 3번 이미지를 더해서 이미지 목구
restored = laplacian + Down_to_Upimg

images = [img, Down_to_Upimg, laplacian, restored]

merged = np.hstack(images)
cv2.imshow('Laplacian Pyramid', merged)
cv2.waitKey(0)
cv2.destroyAllWindows()
'''

'''
# 영상 회전
cp = (w//2, h//2)
rot = cv2.getRotationMatrix2D(cp, 90,2 )
print(rot)
dst = cv2.warpAffine(src, rot, (0,0))

'''

win_name = "scanning"
img = cv2.imread("images/paper2.jpeg", cv2.IMREAD_GRAYSCALE)

if img is None:
    print('Image load failed!')
    sys.exit()

rows, cols = img.shape[:2]
draw = img.copy()
pts_cnt = 0
pts = np.zeros((4, 2), dtype=np.float32)

def onMouse(event, x, y, flags, param):
    global pts_cnt
    if event == cv2.EVENT_LBUTTONDOWN:
        # 좌표에 초록색 동그라미 표시
        cv2.circle(draw, (x, y), 10, (0, 255, 0), -1)
        cv2.imshow(win_name, draw)

        # 마우스 좌표 저장
        pts[pts_cnt] = [x, y]
        pts_cnt += 1
        if pts_cnt == 4:
            # 좌표 4개 중 상하좌우 찾기
            sm = pts.sum(axis=1)  # 4쌍의 좌표 각각 x+y 계산
            diff = np.diff(pts, axis=1)  # 4쌍의 좌표 각각 x-y 계산

            topLeft = pts[np.argmin(sm)]  # x+y가 가장 값이 좌상단 좌표
            bottomRight = pts[np.argmax(sm)]  # x+y가 가장 큰 값이 우하단 좌표
            topRight = pts[np.argmin(diff)]  # x-y가 가장 작은 것이 우상단 좌표
            bottomLeft = pts[np.argmax(diff)]  # x-y가 가장 큰 값이 좌하단 좌표

            # 변환 전 4개 좌표 
            pts1 = np.float32([topLeft, topRight, bottomRight, bottomLeft])

            # 변환 후 영상에 사용할 서류의 폭과 높이 계산
            w1 = abs(bottomRight[0] - bottomLeft[0])
            w2 = abs(topRight[0] - topLeft[0])
            h1 = abs(topRight[1] - bottomRight[1])
            h2 = abs(topLeft[1] - bottomLeft[1])
            width = max([w1, w2])  # 두 좌우 거리간의 최대값이 서류의 폭
            height = max([h1, h2])  # 두 상하 거리간의 최대값이 서류의 높이

            # 변환 후 4개 좌표
            pts2 = np.float32([[0, 0], [width - 1, 0],
                               [width - 1, height - 1], [0, height - 1]])

            # 변환 행렬 계산 
            mtrx = cv2.getPerspectiveTransform(pts1, pts2)
            # 원근 변환 적용
            result = cv2.warpPerspective(img, mtrx, (width, height))
            cv2.imshow('scanned', result)

cv2.imshow(win_name, img)
cv2.setMouseCallback(win_name, onMouse)
cv2.waitKey(0)
cv2.destroyAllWindows()






# images = [src, dst]
# merged = np.hstack(images)
# cv2.imshow('images', merged)

