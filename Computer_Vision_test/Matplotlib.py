from matplotlib import pyplot as plt
import cv2

img = cv2.imread('lena.jpg',-1)
cv2.imshow('Image',img)   # read image in ' BGR 'format
# plt.imshow(img)           # read image in ' RBG ' format
# plt.show()

img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
plt.xticks([]), plt.yticks([])   # hide x y axis
plt.imshow(img)
plt.show()

th1 = cv2.imread('D:/Charles/Picture/A.PNG')
th2 = cv2.imread('D:/Charles/Picture/I know.PNG')
th3 = cv2.imread('D:/Charles/Picture/J.PNG')
th4 = cv2.imread('D:/Charles/Picture/u.PNG')
th5 = cv2.imread('D:/Charles/Picture/To the Moon & Back.PNG')

titles = ['P1','P2','P3','P4','P5','P6 ']
images = [img, th1, th2, th3, th4, th5 ]

for i in range(6):
    plt.subplot(2,3, i+1), plt.imshow(images[i], 'gray')
    plt.title(titles[i])

plt.show()

