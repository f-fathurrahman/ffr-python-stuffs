import cv2
import numpy as np
import sys

if len(sys.argv) < 2:
    raise RuntimeError("Need one argument")

img = cv2.imread(sys.argv[1])

Nrows, Ncols = img.shape[:2]

src_points = np.float32([
    [0, 0],
    [Ncols-1,0],
    [0,Nrows-1]
])
dst_points = np.float32([
    [0, 0],
    [int(0.6*(Ncols-1)), 0],
    [int(0.4*(Ncols-1)), Nrows-1]
])

affine_matrix = cv2.getAffineTransform(src_points, dst_points)
img_output = cv2.warpAffine(img, affine_matrix, (Nrows, Ncols))

cv2.imshow("Input", img)
cv2.imshow("Output", img_output)

cv2.waitKey()
