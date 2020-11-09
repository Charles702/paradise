import cv2
import numpy as np

img = cv2.imread('messi5.jpg')
img2 = cv2.imread('opencv-logo.png')

print(img.shape)
print(img.size)
print(img.dtype)
b,g,r = cv2.split(img)

'''
  1. copy ball
   
'''
ball = img[280:340, 330:390]
img[273:333, 100:160] = ball

img = cv2.resize(img,(512,512))
img2 = cv2.resize(img2, (512,512))

dst = cv2.add(img, img2)
dst1 = cv2.addWeighted(img, 0.9, img2, 0.2, 2);


'''
   2. bitwise 
'''
#bit = cv2.bitwise_and(img, img2)

#img1 = cv2.merge((b,g,r))
cv2.imshow('Messi', dst)
cv2.waitKey(0)

'''
  3.  Trackbar  
'''
img4 = np.zeros((300,512,3), np.uint8)
cv2.namedWindow('TrackBar')

def changebar (x):
    print(x)

cv2.createTrackbar('B','TrackBar',0, 255, changebar)
cv2.createTrackbar('G','TrackBar',0, 255, changebar)
cv2.createTrackbar('R','TrackBar',0, 255, changebar)

while(1):
    cv2.imshow('TrackBar', img4)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        print(ord('q'))
        break
    b = cv2.getTrackbarPos("B", 'TrackBar')
    g = cv2.getTrackbarPos("G", 'TrackBar')
    r = cv2.getTrackbarPos("R", 'TrackBar')

    img4[:] = [b, g, r]

cv2.destroyAllWindows()

'''
  4. HSV hue saturation value :  Cylindrical model
     Hue 0-360: colour component 
     Saturation : 0-100% depth of colour 
     value:  0 - 100% brightness 
'''
def nothing(x):
    pass

cap = cv2.VideoCapture(0);
cv2.namedWindow("Trackbar")
cv2.createTrackbar("Lhue","Trackbar", 0,255, nothing)
cv2.createTrackbar("LS","Trackbar", 0,255, nothing)
cv2.createTrackbar("LV","Trackbar", 0,255, nothing)
cv2.createTrackbar("Hhue","Trackbar", 255,255, nothing)
cv2.createTrackbar("HS","Trackbar", 255,255, nothing)
cv2.createTrackbar("HV","Trackbar", 255,255, nothing)



#---different code for HSV
#print(hsv)
# print(frame)

while True:
    '''
    mask the image
    frame = cv2.imread('D:/Program Files/opencv-master/samples/data/smarties.png')
    '''
    #------ mask video stream--------
    _, frame = cap.read()

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
   # l_b = np.array([110, 50, 50])
   # u_b = np.array([130, 255, 255])

    # Get HSV value from trackbar
    l_h = cv2.getTrackbarPos('Lhue',"Trackbar")
    l_s = cv2.getTrackbarPos('LS', "Trackbar")
    l_v = cv2.getTrackbarPos('LV', "Trackbar")

    u_h = cv2.getTrackbarPos('Hhue', "Trackbar")
    u_s = cv2.getTrackbarPos('HS', "Trackbar")
    u_v = cv2.getTrackbarPos('HV', "Trackbar")

    # Set mask range
    l_b = np.array([l_h, l_s, l_v])
    u_b = np.array([u_h, u_s, u_v])
    mask  = cv2.inRange(hsv, l_b, u_b)
    res = cv2.bitwise_and(frame, frame, mask=mask)

    cv2.imshow('frame', frame)
    cv2.imshow('mask', mask)
    cv2.imshow('res', res)

    key = cv2.waitKey(1)
    if key == 113:
        break

cap.release()
cv2.destroyAllWindows()

