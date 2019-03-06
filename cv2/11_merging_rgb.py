import cv2
import sys

if len(sys.argv) < 2:
    raise RuntimeError("Need one argument")

fname = sys.argv[1].split("/")[-1]
print("fname = ", fname)

img = cv2.imread(sys.argv[1], cv2.IMREAD_COLOR)

cv2.imshow("Original image", img)

print("\nOriginal (RGB):")
print(type(img))
print(img.shape)
print(img.dtype)

g, b, r = cv2.split(img)

img_gbr = cv2.merge((g, b, r))
img_rbr = cv2.merge((r, b, r))
img_rgb = cv2.merge((r, g, b))
img_ggr = cv2.merge((g, g, r))
img_gbg = cv2.merge((g, b, g))

cv2.imshow("GBR", img_gbr)
cv2.imshow("RBR", img_rbr)
cv2.imshow("RGB", img_rgb)
cv2.imshow("GGR", img_ggr)
cv2.imshow("GBG", img_gbg)

cv2.waitKey(0)
