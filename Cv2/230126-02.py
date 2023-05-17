import matplotlib.pyplot as plt
import cv2
import sys
import numpy as np

cap1 = cv2.VideoCapture('woman.mp4')

# 에러 안전장치
if not cap1.isOpened():
    print('video open failed!')
    sys.exit()

cap2 = cv2.VideoCapture('raining.mp4')

if not cap2.isOpened():
    print('video open failed!')
    sys.exit()

cap3 = cv2.VideoCapture('monkey.mp4')

if not cap3.isOpened():
    print('video open failed!')
    sys.exit()

cap4 = cv2.VideoCapture('elephant.mp4')

if not cap4.isOpened():
    print('video open failed!')
    sys.exit()

# 두 영상의 크기, FPS는 같다고 가정
w = round(cap1.get(cv2.CAP_PROP_FRAME_WIDTH))
h = round(cap1.get(cv2.CAP_PROP_FRAME_HEIGHT))
frame_cnt1 = round(cap1.get(cv2.CAP_PROP_FRAME_COUNT))
frame_cnt2 = round(cap1.get(cv2.CAP_PROP_FRAME_COUNT))
fps = round(cap1.get(cv2.CAP_PROP_FPS))

# 프레임 간 시간 간격 설정
delay = int(2000/fps)

# 합성 여부 플래그
do_composit = False
comlist = ['m1', 'm2', 'm3']
i = 0
#전체 동영상 재생
while True:
    ret1, frame1 = cap1.read() # 녹색 배경 영상 읽어오기

    if not ret1: # 영상 1 프레임이 끝나면 종료
        break

    # true일 때에만 합성
    if do_composit:
        # HSV 색 공간에서 녹색 영역을 검출하여 합성
        hsv = cv2.cvtColor(frame1, cv2.COLOR_BGR2HSV)
        mask = cv2.inRange(hsv, (50, 150, 0), (70, 255, 255)) # 영상 최솟값, 최대값

        if i == 3:
            i == 0

        if comlist[i] == 'm1':
            ret2, frame2 = cap2.read() # 비오는 영상 불러오기
            cv2.copyTo(frame2, mask, frame1)

        if comlist[i] == 'm2':
            ret3, frame3 = cap3.read()
            cv2.copyTo(frame3, mask, frame1)

        
        if comlist[i] == 'm3':
            ret4, frame4 = cap4.read()
            cv2.copyTo(frame4, mask, frame1)


    cv2.imshow('frame', frame1)
    key = cv2.waitKey(delay)

    if key == ord(' '): # 스페이스 바를 누르면 true가 됨, 계속 바뀔 수 있게
        do_composit = not do_composit
    
    elif key == 27: # Esc 종료 버튼
        break

    if key == ord('i'):
        i += 1
        if i == 3:
            i == 0

cap1.release()
cap2.release()
cv2.destroyAllWindows( )
