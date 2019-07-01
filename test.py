# -*- coding: utf-8 -*-


import numpy as np
from scipy import ndimage
import cv2

# y1 = np.load("aa.npy")
# # y1 = ndimage.binary_fill_holes(y1)
# # y1_img = ndimage.binary_opening(y1, iterations=10)
# img2 = y1.astype('uint8')*255
# # print(img2.shape)
# cv2.imshow('im', img2)
# cv2.waitKey(5000)

y1 = np.load("aa.npy")
img = y1.astype('uint8')*255

y1 = ndimage.binary_fill_holes(y1)
y1_img = ndimage.binary_opening(y1, iterations=10)
y1_img = y1_img.astype('uint8')*255

color = cv2.cvtColor(y1_img, cv2.COLOR_GRAY2BGR) 
# ret, binary = cv2.threshold(y1_img,127,255,cv2.THRESH_BINARY)
im, contours, hierarchy = cv2.findContours(y1_img,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
cv2.drawContours(color, contours, -1, (0, 255, 0), 2)
print((contours))
# cv2.drawContours(color, contours[0], -1, (0,0,255), 3)  

# cv2.imshow('im1', img)
cv2.imshow('im2', y1_img)
cv2.imshow('im3', color)
cv2.waitKey(10000)

