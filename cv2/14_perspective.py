import cv2
import numpy as np
import sys

if len(sys.argv) < 2:
    raise RuntimeError("Need one argument")

img = cv2.imread(sys.argv[1])
Nrows, Ncols = img.shape[:2]

src_points = np.float32([
    [0, 0],
    [Ncols-1, 0],
    [0, Nrows-1],
    [Ncols-1, Nrows-1]
])

dst_points = np.float32([
    [0, 0],
    [Ncols-1, 0],
    [int(0.33*Ncols), Nrows-1],
    [int(0.66*Ncols), Nrows-1]
])

projective_matrix = cv2.getPerspectiveTransform(src_points, dst_points)
img_output = cv2.warpPerspective(img, projective_matrix, (Ncols,Nrows))

cv2.imshow("Input", img)
cv2.imshow("Output", img_output)

cv2.waitKey()

