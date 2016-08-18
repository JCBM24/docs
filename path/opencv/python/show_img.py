#!/usr/bin/env python3
import cv2
import os.path
import sys

imgPath = sys.argv[1]
if not os.path.isfile(imgPath):
    print("usage: show_img.py <file>")
    sys.exit()

img = cv2.imread(imgPath)
cv2.imshow('image', img)
cv2.waitKey(0)
