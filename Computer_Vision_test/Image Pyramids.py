import cv2
import numpy as np

img = cv2.imread('lena.jpg')
# ir1 = cv2.pyrDown(img)   # pyrdown causes losing resolution of image
# ir2 = cv2.pyrDown(ir1)
# hr2 = cv2.pyrUp(ir2)
'''
Gaussian pyramid 
'''
# layer = img.copy()
# gp = [layer]
# for i in range(4):
#     layer = cv2.pyrDown(layer)
#     gp.append(layer)
#     cv2.imshow(str(i), layer)

'''
  Laplacian pyramid:
  A level in Laplacian Pyramid is formed by the difference between that
  level in Gaussian Pyramid and expanded version of its upper level in Gaussian Pyramid
'''
# layer = gp[3]  # up level of Gaussian Pyramid
# lp = [layer]
#
# for i in range(3, 0, -1):
#     gaussian_extend = cv2.pyrUp(gp[i])
#     laplacian = cv2.subtract(gp[i-1], gaussian_extend)
#     #cv2.imshow(str(i), laplacian)
#
#
# cv2.imshow('Original image', img)
# # cv2.imshow('pyrDown 1 image', ir1)
# # cv2.imshow('pryDown 2 image', ir2)
# # cv2.imshow('pryUp 3 image', hr2)
# cv2.waitKey(0)
# cv2.destroyAllWindows()




'''
Image blending  via image pyramid 

1. load the two images of apple and orange
2. Find Gaussian Pyramid for apply and orange
3. from Gaussian Pyramid, find their Lapalacian Pyramids
4. Now joint the left half of apple and right half of orange in each level of 
   Laplacian Pyramids
5. Finally from the joint image pyramids, reconstruct the original image. 

'''
apple = cv2.imread('D:/Program Files/opencv-master/samples/data/apple.jpg')
orange = cv2.imread('D:/Program Files/opencv-master/samples/data/orange.jpg')

# generate Gaussian pyramid for apple/ orange
apple_copy = apple.copy()
gp_apple = [apple_copy]
for i in range(6):
    apple_copy = cv2.pyrDown(apple_copy)
    gp_apple.append(apple_copy)
    # cv2.imshow('apple_copy', apple_copy)
    # cv2.waitKey(0)

orange_copy =  orange.copy()
gp_orange = [orange_copy]
for i in range(6):
    orange_copy = cv2.pyrDown(orange_copy)
    gp_orange.append(orange_copy)
    # cv2.imshow('orange_copy', orange_copy)
    # cv2.waitKey(0)



#genearate Lapalacian Pyramid for apple / orange
apple_copy = gp_apple[5]
lp_apple = [apple_copy]
for i in range(5, 0, -1):
    gaussian_expanded = cv2.pyrUp(gp_apple[i])
    laplacian = cv2.subtract(gp_apple[i-1], gaussian_expanded)
    lp_apple.append(laplacian)

orange_copy = gp_apple[5]
lp_orange = [orange_copy]
for i in range(5,0, -1):
    gaussian_expanded = cv2.pyrUp(gp_orange[i])
    laplacian = cv2.subtract(gp_orange[i-1], gaussian_expanded)
    lp_orange.append(laplacian)

#now add left and right halves of images in each level
print(len(lp_apple))
print(len(lp_orange))
apple_orange_pyramid = []
n = 0
for apple_lap, orange_lap in zip(lp_apple, lp_orange):
    n+=1
    cols, rows, ch = apple_lap.shape

    # cv2.imshow('apple_lap', apple_lap)
    # cv2.imshow('orange_lap', orange_lap)
    # cv2.waitKey(0)

    laplacian = np.hstack((apple_lap[:, 0:int(cols/2)], orange_lap[:, int(cols/2):]))
    cv2.imshow('laplacian', laplacian)
    cv2.waitKey(0)
    apple_orange_pyramid.append(laplacian)

# now reconstruct
apple_orange_reconstruct = apple_orange_pyramid[0]
for i in range(1,6):
    apple_orange_reconstruct = cv2.pyrUp(apple_orange_reconstruct)
    apple_orange_reconstruct = cv2.add(apple_orange_pyramid[i], apple_orange_reconstruct)
    cv2.imshow('apple_orange_reconstruct', apple_orange_reconstruct)
    cv2.waitKey(0)

apple_orange = np.hstack((apple[:, :256], orange[:, 256:]))
cv2.imshow('apple', apple)
cv2.imshow('orange', orange)
cv2.imshow("apple_orange", apple_orange)
cv2.imshow('apple_orange_reconstruct',apple_orange_reconstruct)

cv2.waitKey(0)
cv2.destroyAllWindows()

