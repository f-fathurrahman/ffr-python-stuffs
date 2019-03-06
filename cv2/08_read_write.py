import cv2
import sys

if len(sys.argv) < 2:
    raise RuntimeException("Need one argument")

fname = sys.argv[1].split("/")[-1]
print("fname = ", fname)

img = cv2.imread(sys.argv[1])

cv2.imshow("Original image", img)

print("\nOriginal:")
print(type(img))
print(img.shape)
print(img.dtype)

img_gray = cv2.imread(sys.argv[1], cv2.IMREAD_GRAYSCALE)

cv2.imshow("Grayscale image", img_gray)

print("\nGrayscale:")
print(type(img_gray))
print(img_gray.shape)
print(img.dtype)

cv2.imwrite("images/TEMP_" + fname, img_gray)

cv2.waitKey()

