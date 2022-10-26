import cv2
import numpy as np


photo = cv2.imread("bird.jpg",0)
cv2.imshow("bird.jpg",photo)
cv2.waitKey()

histogramSize = 256
histogramRange = (0, 256)

histogram = np.zeros(256)
width,height = photo.shape

for i in range(0, width):
    for j in range(0,height):
         index = photo[i,j]
         histogram[index] = histogram[index] + 1

for i,index in enumerate(histogram):
    print(f"{i} -> {index}")

from matplotlib import pyplot as plt
plt.plot(histogram)
plt.show()
cv2.waitKey()
