import cv2
import sys

if len(sys.argv) < 2:
    raise RuntimeError("Need one argument")

fname = sys.argv[1].split("/")[-1]
print("fname = ", fname)

img = cv2.imread(sys.argv[1])

cv2.imshow("Original image", img)

print("\nOriginal:")
print(type(img))
print(img.shape)
print(img.dtype)

fname_png = fname.replace(".jpg", ".png")
cv2.imwrite("images/TEMP_" + fname_png, img, [cv2.IMWRITE_PNG_COMPRESSION])

cv2.waitKey(0)