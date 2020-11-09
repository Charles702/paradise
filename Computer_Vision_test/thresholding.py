'''
1. sample image thresholding
2. adaptive Thresholding
'''
import numpy as ny
import cv2

img = cv2.imread('D:/Program Files/opencv-master/samples/data/gradient.png', 0)
_,a1 = cv2.threshold(img, 50, 255, cv2.THRESH_BINARY)
_,a2 = cv2.threshold(img, 50, 255, cv2.THRESH_BINARY_INV)
_,a3 = cv2.threshold(img, 50, 255, cv2.THRESH_TRUNC)
_,a4 = cv2.threshold(img, 50, 255, cv2.THRESH_TOZERO)
_,a5 = cv2.threshold(img, 50, 255, cv2.THRESH_TOZERO_INV)

cv2.imshow('Original Image', img)
cv2.imshow('th1', a1)
cv2.imshow('th2', a2 )
cv2.imshow('th3', a3)
cv2.imshow('th4', a4)
cv2.imshow('th5', a5)

cv2.waitKey(0)
cv2.destroyAllWindows()

'''
ADAPTIVE_THRESH_MEAN_C:  the threshold value T(x,y) is a mean of the blockSize×blockSize neighborhood of (x,y) minus C

ADAPTIVE_THRESH_GAUSSIAN_C: the threshold value T(x,y) is a weighted sum (cross-correlation with a Gaussian window) of the blockSize×blockSize 
neighborhood of (x,y) minus C . The default sigma (standard deviation) is used for the specified blockSize
'''
img2 = cv2.imread('D:/Program Files/opencv-master/samples/data/sudoku.png',0)
_,th = cv2.threshold(img2,127,255,cv2.THRESH_BINARY)
a = cv2.adaptiveThreshold(img2, 180, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 2)
b = cv2.adaptiveThreshold(img2, 180, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)

cv2.imshow('Sudoku',img2)
cv2.imshow('simple thresholding',th)
cv2.imshow('mean_c',a)
cv2.imshow('gausian',b)

cv2.waitKey(0)
cv2.destroyAllWindows()



