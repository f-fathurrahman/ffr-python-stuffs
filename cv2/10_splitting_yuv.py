import cv2
import sys

if len(sys.argv) < 2:
    raise RuntimeError("Need one argument")

fname = sys.argv[1].split("/")[-1]
print("fname = ", fname)

img = cv2.imread(sys.argv[1])

cv2.imshow("Original image", img)

print("\nOriginal (RGB):")
print(type(img))
print(img.shape)
print(img.dtype)

img_yuv = cv2.cvtColor(img, cv2.COLOR_BGR2YUV)
print("\nYUV:")
print(type(img_yuv))
print(img_yuv.shape)
print(img_yuv.dtype)

# Split into yuv
y, u, v = cv2.split(img_yuv)
cv2.imshow('Y channel', y)
cv2.imshow('U channel', u)
cv2.imshow('V channel', v)

# Faster
"""
cv2.imshow('Y channel', img_yuv[:,:,0])
cv2.imshow('U channel', img_yuv[:,:,1])
cv2.imshow('V channel', img_yuv[:,:,2])
"""

cv2.waitKey(0)
