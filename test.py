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
cv2.imshow('im1', img)
cv2.imshow('im2', y1_img)
cv2.waitKey(10000)

