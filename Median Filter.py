import cv2

img = cv2.imread('do1.jpg')
img = cv2.resize(img, (400, 450))

filtered_img = cv2.medianBlur(img, 5)

cv2.imshow('Gambar asli', img)
cv2.imshow('Gambar hasil filter', filtered_img)
cv2.waitKey(0)
cv2.destroyAllWindows()