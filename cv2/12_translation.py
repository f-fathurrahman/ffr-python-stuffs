import cv2
import numpy as np
import sys

if len(sys.argv) < 2:
    raise RuntimeError("Need one argument")

img = cv2.imread(sys.argv[1])
Nrows, Ncols = img.shape[:2]

translation_matrix = np.float32([
    [1, 0, 70],
    [0, 1, 110]
    ])
img_translated = cv2.warpAffine(img, translation_matrix, (Nrows,Ncols), cv2.INTER_LINEAR)

cv2.imshow("Original", img)
cv2.imshow("Translation", img_translated)

cv2.waitKey()




