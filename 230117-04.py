import cv2
import sys
import matplotlib.pyplot as plt
import numpy as np

img = cv2.imread('images/person.jpg')
notface_img = img.copy()


face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
faces = face_cascade.detectMultiScale(notface_img, 1.3, 5)

# for x, y, w, h in faces:
#     detected_face = img[int(y):int(y+h), int(x):int(x+w)]
#     detected_face_blr = cv2.GaussianBlur(detected_face, (0, 0), 8)
#     img[y:y+h, x:x+w] = detected_face_blr
#     cv2.imshow('face', detected_face)
notface_blr = cv2.GaussianBlur(img, (0, 0), 8)

for x, y, w, h in faces:
    detected_face = notface_img[int(y):int(y+h), int(x):int(x+w)]
    notface_blr[y:y+h, x:x+w] = detected_face
    cv2.imshow('face', notface_blr)



# x, y, w, h = cv2.selectROI('img', img, False)

# roi = img[y:y+h, x:x+w]
# roi_blur = cv2.GaussianBlur(roi, (0, 0), 7)
# img[y:y+h, x:x+w] = roi_blur

cv2.imshow('img', detected_face)



cv2.waitKey()
cv2.destroyAllWindows()