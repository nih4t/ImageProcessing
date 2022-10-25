import cv2
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import pyplot as plt


foto = cv2.imread("bird.jpg")
cv2.imshow("bird", foto)


B = foto[:,:,0] #blue
G = foto[:,:,1] #green
R = foto[:,:,2] #red

cv2.imshow("blue bird", B)
cv2.imshow("green bird", G)
cv2.imshow("red bird", R)

cv2.waitKey()

#print intensity of image

print(foto.shape)
print(R.shape)

x = 0
y = 0
k = 0

intensity_rgb = foto[y,x,k]
print("intensity = " , intensity_rgb)

intensity_r = R[y,x]
print("intensity_gray= ", intensity_r)

intensity_g = G[y,x]
print("intensity_gray2= ", intensity_g)

intensity_b = B[y,x]
print("intensity_gray3= ", intensity_b)

max_intensity = np.max(B)
print("intensity= ", max_intensity)

min_intensity = np.min(B)
print("intensity= ", min_intensity)

print(foto[y,x])

piece= R[20:30,40:50]
print("piece= " ,piece)

colorful = cv2.imread("bird.jpg")
gray= cv2.imread("bird.jpg", 0 )

cv2.imshow("gray bird", gray)
histColor = cv2.calcHist(colorful, [0], None, [256], [0,256])
histGray  = cv2.calcHist(gray, [0], None, [256], [0,256])

plt.figure(2, facecolor= "purple")
plt.plot(histGray)

B = colorful[:,:,0]
hist_B = cv2.calcHist([B], [0], None, [256], [0,256])

print(np.sum(hist_B))

plt.figure(3, facecolor= "purple")
plt.hist(gray.ravel(), 256, [0,256])
plt.show()
