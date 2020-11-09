import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('D:/Charles/Picture/A.PNG', cv2.IMREAD_GRAYSCALE)
lap = cv2.Laplacian(img, cv2.CV_64F, ksize= 3)
lap = np.uint8(np.absolute(lap))

sobelx =  cv2.Sobel(img, cv2.CV_64F, 1, 0) #vertical edge
sobely =  cv2.Sobel(img, cv2.CV_64F, 0, 1) #horizontal edge
sobelx = np.uint8(np.absolute(sobelx))
sobely = np.uint8(np.absolute(sobely))

sobelCombined = cv2.bitwise_or(sobelx, sobely)

'''
Canny Edge Detection 
'''
canny = cv2.Canny(img, 100, 200)

titles = ['image','Laplacian','Sobelx', 'Sobely','sobelcomined','Canny']
imges = [img, lap, sobelx, sobely,sobelCombined, canny]

for i in range(len(imges)):
    plt.subplot(2,3, i+1), plt.imshow(imges[i],'gray')
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])

plt.show()

