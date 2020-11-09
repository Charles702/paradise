
# python -m pip install --upgrade opencv-python 解决suggestion不显示问题
import cv2
import numpy as np
import datetime as dt

img  = cv2.imread('lena.jpg', -1)

#draw img by numpy
img = np.zeros([512,521,3], np.uint8)
#img = cv2.polylines(img,(1,1,3,2),True,(255,0,0),7)
#print(img)

img = cv2.line(img,(0,0),(255,255),(255,0,0), 4)
img = cv2.arrowedLine(img,(0,0),(255,255),(14,67,178), 4)

#rectangle
img = cv2.rectangle(img, (0,0), (510,128), (14,67,178), -1)
img = cv2.circle(img, (200,200),100, (32,6,22), 19)
font = cv2.FONT_HERSHEY_COMPLEX
img = cv2.putText(img, 'Opencv', (100,200),font, 4, (255,255,0), 10, cv2.LINE_AA)

cv2.imshow('image',img)
cv2.waitKey(5000)
cv2.destroyAllWindows()

cv2.imwrite('beauty.png', img)


 # video stream
# cap = cv2.VideoCapture(0)
# fourcc = cv2.VideoWriter_fourcc(*'XVID')
# out = cv2.VideoWriter('Myvideo.avi', fourcc, 20.0, (640,480))
#
# cap.set(3,1208)
# cap.set(4, 720)
#
# print(cap.get(3))   # change to default resolution
# print(cap.get(4))
#
# while(cap.isOpened()):
#     ret, frame = cap.read()
#     if ret == True:
#         out.write(frame)
#         #gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
#         text = 'Width:'+ str(cap.get(3))+ 'height: '+ str(cap.get(4))
#         timenow = str(dt.datetime.now())
#
#         frame = cv2.putText(frame, timenow, (10,50), font, 1, (0,255,255), 2)
#         cv2.imshow('frame', frame)
#
#         if cv2.waitKey(1) & 0xFF == ord('q'):
#             break
#     else:
#         break
# cap.release()
# out.release()
# cv2.destroyAllWindows()


#--- manipulate mouse

events = [i for i in dir(cv2) if 'EVENT' in i]
print(events)

def click_event(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        print(x,',',y)
        font = cv2.FONT_HERSHEY_COMPLEX
        strXY = str(x)+','+str(y)
        cv2.putText(img1, strXY, (x, y), font, 1, (255,0,0), 2)
        cv2.imshow('image', img1)
    if event == cv2.EVENT_RBUTTONDOWN:
        blue = img[y, x, 0]            # get BGR blue channel
        green = img[y, x, 1]           # get BGR green channel
        red = img[y, x, 2]             # get BGR red channel
        bgr = str(blue)+','+str(green)+', '+str(red)
        cv2.putText(img1, bgr, (x, y), cv2.FONT_HERSHEY_PLAIN, 1, (0,0,255), 2)
        cv2.imshow('image', img1)

img1 = img
#img1 = np.zeros((512,512,3), np.uint8)
cv2.imshow('image', img1)

cv2.setMouseCallback('image', click_event)
cv2.waitKey(0)
#cv2.destroyAllWindows()

#------------------------------------
img3 = np.zeros((512, 512,3), np.uint8)
#img3 = cv2.imread('lena.jpg')
cv2.imshow('picture', img3)
points = []
print('123')
def my_click(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.circle(img3, (x,y), 5, (0,0,255), -1)
        points.append((x,y))
        if len(points) >=2:
            cv2.line(img3, points[-1], points[-2], (255,0,0), 5)  # -1 is last element, , -2 s last second emement

        cv2.imshow("picture", img3)

def my_click1(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        blue = img3[x, y, 0]
        green = img3[x, y, 1]
        red = img3[x, y, 2]
        cv2.circle(img3, (x, y), 5, (0, 0, 255), -1)
        mycolourimage = np.zeros((500,500,3), np.uint8)

        mycolourimage[:] = (blue, green, red)
        cv2.imshow("color", mycolourimage)

cv2.setMouseCallback('picture', my_click)
cv2.waitKey(0)

x = np.zeros((3,3,2), np.uint8)
print (x)
