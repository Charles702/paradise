import cv2
from matplotlib import pyplot as plt

Aj1 = cv2.imread('D:/Charles/Picture/AJ1.jpg')
Aj2 = cv2.imread('D:/Charles/Picture/AJSlam.jpg')
Aj3 = cv2.imread('D:/Charles/Picture/AJ3.jpg')
Aj4 = cv2.imread('D:/Charles/Picture/AJ4.jpg')
Aj5 = cv2.imread('D:/Charles/Picture/AJ5.jpg')
Aj6 = cv2.imread('D:/Charles/Picture/AJ6.jpg')
Aj7 = cv2.imread('D:/Charles/Picture/AJ7.jpg')
Aj8 = cv2.imread('D:/Charles/Picture/AJ8.jpg')
Aj9 = cv2.imread('D:/Charles/Picture/AJ9.jpg')
Aj10 = cv2.imread('D:/Charles/Picture/AJ10.jpg')
Aj11 = cv2.imread('D:/Charles/Picture/AJ11.jpg')
Aj12 = cv2.imread('D:/Charles/Picture/AJ12.jpg')
Aj13 = cv2.imread('D:/Charles/Picture/AJ11.jpg')
Aj12 = cv2.imread('D:/Charles/Picture/AJ12.jpg')
Aj13 = cv2.imread('D:/Charles/Picture/AJ13.jpg')
Aj14 = cv2.imread('D:/Charles/Picture/AJ14.jpg')
Aj15 = cv2.imread('D:/Charles/Picture/AJ15.jpg')
Aj16 = cv2.imread('D:/Charles/Picture/AJ16.jpg')
Aj17 = cv2.imread('D:/Charles/Picture/AJ17.jpg')
Aj18 = cv2.imread('D:/Charles/Picture/AJ18.jpg')
Aj19 = cv2.imread('D:/Charles/Picture/AJ19.jpg')


images = [Aj1, Aj2,Aj3,Aj4,Aj5,Aj6,Aj7,Aj8,Aj9,Aj10, Aj11, Aj12, Aj13, Aj14, Aj15, Aj16, Aj17, Aj18, Aj19 ]

for i in range(len(images)):
    print(i)
    images[i] = cv2.cvtColor(images[i], cv2.COLOR_BGR2RGB)

for i in range(18):
    plt.subplot(3, 6, i+1)
    plt.imshow(images[i],'gray')
    plt.title( 'Air Jordan'+ str(i))

plt.show()