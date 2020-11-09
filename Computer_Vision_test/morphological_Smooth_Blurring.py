import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('D:/Program Files/opencv-master/samples/data/smarties.png', cv2.IMREAD_GRAYSCALE)

_, mask = cv2.threshold(img, 220, 255, cv2.THRESH_BINARY_INV)

kernal = np.ones((5,5), np.uint8)
print(kernal)
dialation = cv2.dilate(mask, kernal, iterations = 2)
erosion =  cv2.erode(mask, kernal, iterations=1)
opening = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernal)  # erosion ->  dilation
closing = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernal)  # dialation  ->   erosion
gd = cv2.morphologyEx(mask, cv2.MORPH_GRADIENT, kernal)
th = cv2.morphologyEx(mask, cv2.MORPH_TOPHAT, kernal) # difference between input image and opening image


titles  = ['image', 'mask', 'Dialate', 'Erode', 'open','closing', 'gd', 'th']
images = [img, mask, dialation, erosion, opening, closing, gd, th]

for i in range(8):
    plt.subplot(2, 4, i+1), plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])

plt.show()

'''
  Smoothing and blurring 
  
  1. Homogeneous filter. each output pixel is the  mean of kernal neighbours
  2. bluring
  3, Gaussian filter : different weight kernal , Gaussian distribution
  4. median filter: replace each pixel's value with median of its neighbour pixels, deal with "sault and pepper nosoe "
  
'''
img = cv2.imread('D:/Program Files/opencv-master/samples/data/HappyFish.jpg')
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

kernel = np.ones((5, 5), np.float32)/25
dst = cv2.filter2D(img, -1, kernel)
blur = cv2.blur(img,(5,5))
gblur = cv2.GaussianBlur(img, (5,5), 0)
median = cv2.medianBlur(img, 5)
bilatralFilter = cv2.bilateralFilter(img, 9, 75, 75)   # remove noise and remain border sharp



titles  = ['image', '2D_conv', 'blur', 'gblur', 'median', 'Bilateral']
images = [img, dst, blur, gblur, median, bilatralFilter]

for i in range(len(images)):
    plt.subplot(2, 3, i+1), plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])

plt.show()



