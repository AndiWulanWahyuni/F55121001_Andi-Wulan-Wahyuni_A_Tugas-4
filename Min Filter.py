import numpy as np
import cv2

def min_filter(image, kernel_size):
    pad_size = kernel_size // 2
    height, width = image.shape
    padded_image = np.zeros((height + 2 * pad_size, width + 2 * pad_size))
    padded_image[pad_size:height+pad_size, pad_size:width+pad_size] = image

    filtered_image = np.zeros((height, width))
    for i in range(pad_size, height + pad_size):
        for j in range(pad_size, width + pad_size):
            roi = padded_image[i-pad_size:i+pad_size+1, j-pad_size:j+pad_size+1]
            min_val = np.min(roi)
            filtered_image[i-pad_size, j-pad_size] = min_val

    return filtered_image.astype(np.uint8)

image = cv2.imread('do2.jpg', cv2.IMREAD_GRAYSCALE)
image = cv2.resize(image, (400, 450))
filtered_image = min_filter(image, 3)
cv2.imshow('Original Image', image)
cv2.imshow('Filtered Image', filtered_image)
cv2.waitKey(0)
cv2.destroyAllWindows()