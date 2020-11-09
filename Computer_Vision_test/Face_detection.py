'''
Haar Cascade Classifiers

'''

import cv2

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')  # face
eye_cascade = cv2.CascadeClassifier('haarcascade_eye_tree_eyeglasses.xml')   #eye

img = cv2.imread('lena.jpg')
gray =cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
faces = face_cascade.detectMultiScale(gray, 1.1, 4)

for (x, y, w, h) in faces:
    cv2.rectangle(img, (x,y), (x + w, y + h), (255,0,0), 3)
    #find eyes
    roi_gray = gray[y:y+h, x:x+w]
    roi_color = img[y:y+h, x:x+w]
    eyes = eye_cascade.detectMultiScale(roi_gray)
    for (ex, ey, ew, eh ) in eyes:
        cv2.rectangle(roi_color, (ex,ey),(ex+ew, ey+eh), (0,0,255), 4)

cv2.imshow('img', img)
cv2.waitKey()

cap = cv2.VideoCapture('C:/Users/62501/Pictures/Camera Roll/WIN_20200518_10_57_45_Pro.mp4')

while cap.isOpened():
    _, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)

    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 3)
    #find eyes
    roi_gray = gray[y:y+h, x:x+w]
    roi_color = img[y:y+h, x:x+w]
    eyes = eye_cascade.detectMultiScale(roi_gray)
    for (ex, ey, ew, eh ) in eyes:
        cv2.rectangle(roi_color, (ex,ey),(ex+ew, ey+eh), (0,0,255), 4)

    cv2.imshow('img', img)
    if cv2.waitKey(1)& 0xFF == ord('q'):
        break
cap.release()

'''
Detect Eyes 

'''



