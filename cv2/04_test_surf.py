import cv2
import matplotlib.pyplot as plt
import sys
import os

img_bgr = cv2.imread( sys.argv[1] )
img_rgb = cv2.cvtColor( img_bgr, cv2.COLOR_BGR2RGB )

surf = cv2.xfeatures2d.SURF_create()

# detect keypoints
kp = surf.detect( img_bgr )

import numpy as np
img_kp = np.zeros_like( img_bgr )
img_kp = cv2.drawKeypoints( img_rgb, kp, img_kp, flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS )

plt.clf()
plt.imshow( img_kp )
FILESAVE = 'TEST_IMG_5.pdf'
plt.savefig(FILESAVE)
os.system('pdfcrop ' + FILESAVE + ' ' + FILESAVE)

# feature descriptor can be computed using
kp, des = surf.compute( img_bgr, kp )

print('des.shape = ', des.shape)

# alternative: detect and compute
# kp2, des2 = sift.detectAndCompute( img_bgr, None )
