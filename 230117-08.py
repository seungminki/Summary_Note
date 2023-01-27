import cv2
import numpy as np

def on_trackbar(pos):
    rmin = cv2.getTrackbarPos('minRadius', 'img')
    rmax = cv2.getTrackbarPos('maxRadius', 'img')
    th = cv2.getTrackbarPos('threshold', 'img')

    circles = cv2.HoughCircles(blr, cv2.HOUGH_GRADIENT, 1, 50, param1=120, 
        param2=th, minRadius=rmin, maxRadius=rmax)

    dst = img.copy()


    if circles is not None:
        for i in range(circles.shape[1]):
            cx, cy, r = np.uint16(circles[0][i])
            cv2.circle(dst, (cx, cy), r, (0, 0, 255), 2, cv2.LINE_AA)

    cv2.imshow('img', dst)


img = cv2.imread('images/coin.jpg')

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
blr = cv2.GaussianBlur(gray, (0, 0), 1.)

cv2.imshow('img', img)
cv2.createTrackbar('minRadius', 'img', 0, 100, on_trackbar)
cv2.createTrackbar('maxRadius', 'img', 0, 150, on_trackbar)
cv2.createTrackbar('threshold', 'img', 0, 100, on_trackbar)

cv2.waitKey()
cv2.destroyAllWindows()