'''
Harris Corner detector

1. determine which windows produce very large variations in intensity when
   move in both X and Y directions
2. With Each such Window found, a score R is computed
3 after applying a threshold to this score,important corners are selected and marked

'''
import cv2
import numpy as np

img = cv2.imread('D:/Program Files/opencv-master/samples/data/ml.png')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gray = np.float32(gray)
cornerset = cv2.cornerHarris(gray,
                  2,    #size of neighbourhood considered for corner detection
                  3,    # Aperture parameter of Sobel derivative used
                  0.04  # Harris detector free parameter in the equation
                 )

print(cornerset)

#dst = cv2.dilate(cornerset, None)

img[cornerset > 0.01* cornerset.max()] = [0, 0, 255]

cv2.imshow('corner', img)


'''
Shi Tomasi Corner Detection: modification base on Haar corner detection 
'''
img2 = cv2.imread('D:/Program Files/opencv-master/samples/data/ml.png')
gray2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

corners = cv2.goodFeaturesToTrack(gray2, 20, 0.01, 10)

corners = np.int0(corners)

for i in corners:
    x, y = i.ravel()
    cv2.circle(img2, (x,y), 3, 255, -1)  # -1 means fill the circle with the color

cv2.imshow('output', img2)

if cv2.waitKey(0)&0xff ==  ord('q'):
    cv2.destroyAllWindows()
