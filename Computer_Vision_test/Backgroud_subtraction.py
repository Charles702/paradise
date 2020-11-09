import numpy as np
import cv2
cap = cv2.VideoCapture('Crowed.mp4')
#fgbg = cv2.createBackgroundSubtractorMOG2()
fgbg = cv2.createBackgroundSubtractorKNN()
#kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (3,3))


while True:
    ret, frame = cap.read()
    if frame is None:
        break
    fgmask = fgbg.apply(frame)
    #fgmask = cv2.morphologyEx(fgmask, cv2.MORPH_OPEN, kernel)

    cv2.imshow('Frame', frame)
    cv2.imshow('FG_MASK_Frame', fgmask)

    k = cv2.waitKey(30)
    if k == ord('q') or k ==27:
        break

cap.release()
cv2.destroyAllWindows()
