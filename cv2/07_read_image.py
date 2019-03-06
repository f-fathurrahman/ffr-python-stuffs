import cv2
import sys

if len(sys.argv) < 2:
    raise RuntimeException("Need at least one argument")

# Load the image
img = cv2.imread(sys.argv[1])

# Show the image
cv2.imshow("Test image", img)

print(type(img))
print(img.shape)

cv2.waitKey()

