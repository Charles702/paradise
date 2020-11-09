import cv2
import numpy as np

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
    if lines != 'NoneType':
        for line in lines:    # line is represented by first coordiantes and end coordinate
            for x1, y1, x2, y2 in line:
                cv2.line(blank_image, (x1, y1), (x2, y2), (0,255,0), thickness= 3)

        copyimg = cv2.addWeighted(copyimg, 0.8, blank_image, 1, 0.0)
    return copyimg

def process(image_video):
    h = image_video.shape[0]
    w = image_video.shape[1]
    region_of_interest_vertices = [
        (0, h),
        (w / 2, h / 2),
        (w, h / 2),
        (w, h)
    ]
    print(region_of_interest_vertices)
    canny_image2 = cv2.Canny(image_video, 100, 200)
    cropped_image2 = region_of_interest2(canny_image2,  np.array([region_of_interest_vertices], np.int32))

    lines = cv2.HoughLinesP(cropped_image2,
                           rho=6,
                           theta= np.pi/60,
                           threshold=120,
                            lines=np.array([]),
                            minLineLength= 10,
                            maxLineGap= 25)
    print(lines)
    image_with_lines = draw_lines(image_video, lines)
    return image_with_lines


cap =cv2.VideoCapture('test.mp4')

while(cap.isOpened()):
    ret, frame = cap.read()
    frame = process(frame)
    cv2.imshow('Lane', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
