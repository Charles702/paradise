import matplotlib.pylab as plt
import cv2
import numpy as np

def region_of_interest(img, vertices):
    mask = np.zeros_like(img)
    channel_count = img.shape[2]  # obtain channel number
    match_mask_color = (255, ) * channel_count
    print(match_mask_color)
    cv2.fillPoly(mask, vertices, match_mask_color)
    masked_image = cv2.bitwise_and(img, mask)
    return masked_image

def region_of_interest2(img, vertices):
    mask = np.zeros_like(img)
    match_mask_color = 255     # 1 channel
    print(match_mask_color)
    cv2.fillPoly(mask, vertices, match_mask_color)
    masked_image = cv2.bitwise_and(img, mask)
    return masked_image

def draw_lines(img, lines):
    copyimg = np.copy(img)
    blank_image = np.zeros((img.shape[0], img.shape[1],3), dtype = np.uint8)

    for line in lines:    # line is represented by first coordiantes and end coordinate
        for x1, y1, x2, y2 in line:
            cv2.line(blank_image, (x1, y1), (x2, y2), (0,255,0), thickness= 3)

    copyimg = cv2.addWeighted(copyimg, 0.8, blank_image, 1, 0.0)
    return copyimg


image = cv2.imread('road2.jpg')
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

print(image.shape)
h = image.shape[0]
w = image.shape[1]

region_of_interest_vertices = [
    (0, h),
    (w/2, h/2),
    (w, h/2),
    (w, h)

]
cropped_image = region_of_interest(image,
                np.array([region_of_interest_vertices], np.int32) )

#-- 2. find lane --
gray_image = cv2.cvtColor(cropped_image, cv2.COLOR_RGB2GRAY)
canny_image = cv2.Canny(gray_image, 100, 200)

plt.imshow(canny_image)
#plt.imshow(cropped_image)
plt.show()

#---- 3, improved method of finding lane -----
orignal_gray_image = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
canny_image2 = cv2.Canny(orignal_gray_image, 100, 200)
cropped_image2 = region_of_interest2(canny_image2,  np.array([region_of_interest_vertices], np.int32))
plt.imshow(cropped_image2)
plt.show()

lines = cv2.HoughLinesP(cropped_image2,
                       rho=6,
                       theta= np.pi/60,
                       threshold=160,
                        lines=np.array([]),
                        minLineLength= 40,
                        maxLineGap= 25)

image_with_lines = draw_lines(image, lines)
plt.imshow(image_with_lines)
plt.show()



