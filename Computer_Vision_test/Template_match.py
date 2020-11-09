import cv2
import numpy as np

img = cv2.imread("messi5.jpg")
grey_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
print(grey_img.shape)
template = cv2.imread("messi_face.jpg", 0)
cv2.imshow('face',template)
print(template.shape)
w, h = template.shape[::-1]

# dfferent match method "TM_CCORR_NORMED"
res = cv2.matchTemplate(grey_img, template, cv2.TM_CCOEFF_NORMED)

#print(res)
threshold = 0.5
loc = np.where(res >= threshold)
print(loc)
for pt in zip(*loc[::-1]):
    print(pt)
    cv2.rectangle(img, pt, (pt[0] +w, pt[1] +h), (0, 0, 255), 2)

cv2.imshow('img', img)
cv2.waitKey(0)
cv2.destroyAllWindows()