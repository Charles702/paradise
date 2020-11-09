'''
Meanshift Method
Camshift Method
'''
import numpy as np
import cv2

x, y, width, height = 300,200, 80,50  #  718    136
#setup intitial location of window
track_window = (x, y, width, height)


cap = cv2.VideoCapture('traffic1.mp4')
# take first frame of the video
ret, frame = cap.read()

def my_click(event, recx,recy, flag, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        x = recx
        y = recy
        cv2.rectangle(frame, (x, y), (x + width, y + height), 255, 3)
        cv2.imshow('vehicle_location',frame)
        print(x, '  ', y)
        track_window = (x, y, width, height)
        print(track_window)

cv2.imshow('vehicle_location',frame)
cv2.setMouseCallback('vehicle_location', my_click)
cv2.waitKey(0)

#set up the ROI for tracking
roi = frame[y: y+ height, x:x+width]
hsv_roi = cv2.cvtColor(roi, cv2.COLOR_BGR2HSV)
mask = cv2.inRange(hsv_roi, np.array((0, 60, 32)), np.array((180,255,255)))
roi_hist = cv2.calcHist([hsv_roi], [0], mask, [180], [0,180])
cv2.normalize(roi_hist, roi_hist, 0, 255, cv2.NORM_MINMAX)

track_window = (713, 148, 80, 50)
# setup the terminiation criteria, either ten iteration or move by at least 1 pt
term_crit = (cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT, 10, 1)
cv2.imshow('roi', roi)
while(1):
    ret, frame = cap.read()
    if ret == True:
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        dst = cv2.calcBackProject([hsv], [0], roi_hist, [0,180], 1)
        #apply menshift to get new location
        ret, track_window = cv2.meanShift(dst, track_window, term_crit)

        # Draw it on image
        x, y, w, h = track_window
        final_image = cv2.rectangle(frame,(x, y), (x+w,y+h), 255, 3)

        cv2.imshow('dst', dst)
        cv2.imshow('final_image', final_image)

        k = cv2.waitKey(30)
        if k == ord('q') or k == 27:
            break
    else:
        break

cap.release()
cv2.destroyAllWindows()