import cv2
import numpy as np
foto = cv2.imread("bird.jpg")
cv2.imshow("bird.jpg",foto)
cv2.waitKey()

B = foto[:,:,0]
G = foto[:,:,1]
R = foto[:,:,2]

photoGray = cv2.imread("bird.jpg",0)
cv2.imshow("bird.jpg",photoGray)
cv2.waitKey()

from matplotlib import pyplot as plt
import matplotlib.image as mpimg
imgGray = 0.299 * R + 0.587 * G + 0.114 * B
plt.imshow(photoGray, cmap = 'gray')
plt.show()

imgYUV = cv2.cvtColor(foto, cv2.COLORYU_BGR2V)
y, u, v = cv2.split(imgYUV)

cv2.imshow('y', y)
cv2.imshow('u', u)
cv2.imshow('v', v)
cv2.imshow("bird.jpg",imgYUV)
cv2.waitKey(0)