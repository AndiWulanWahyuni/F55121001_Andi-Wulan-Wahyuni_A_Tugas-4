import cv2
import numpy as np

img = cv2.imread('do3.jpg')
img = cv2.resize(img, (400, 450))

gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

kernel_size = 3

max_img = cv2.dilate(gray_img, np.ones((kernel_size,kernel_size), np.uint8))

cv2.imshow("Original Image", img)
cv2.imshow("Maximum Filter Result", max_img)
cv2.waitKey(0)
cv2.destroyAllWindows()