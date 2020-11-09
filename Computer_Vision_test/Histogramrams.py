import numpy as np
import cv2
from matplotlib import pyplot as plt

img = cv2.imread("lena.jpg")
b, g, r = cv2.split(img)
plt.hist(b.ravel(), 256, [0, 256])
plt.hist(g.ravel(), 256, [0, 256])
plt.hist(r.ravel(), 256, [0, 256])
plt.show()

img1 = cv2.imread('messi5.jpg',0)
print(img1.shape)
hist1 = cv2.calcHist([img],[0],None, [256], [0,256])
plt.plot(hist1)
plt.show()