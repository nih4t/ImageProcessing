import cv2
import numpy as np


img = cv2.imread("bird.jpg", 0)
h, w = img.shape
MAX = 0
#find maximum value
for i in range(h):
    for j in range(w):
        if img[i, j] > MAX:
            MAX = img[i, j]

#create empty matrix (same dimensions)
invImg = np.zeros([h, w], dtype=np.uint8)

#inverting
for i in range(h):
    for j in range(w):
        invImg[i, j] = MAX - img[i, j]


cv2.imshow("gray", img)
cv2.imshow("inverted", invImg)

cv2.waitKey()