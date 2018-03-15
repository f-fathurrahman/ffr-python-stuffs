import cv2
import matplotlib.pyplot as plt
import sys
import os

img_bgr = cv2.imread( sys.argv[1] )

img_gray = cv2.cvtColor( img_bgr, cv2.COLOR_BGR2GRAY )

# Using Harris corner detection
# Parameters:
# - an input image
# - the pixel neighborhood size considered for corner detection (blockSize),
# - an aperture parameter for the edge detection (ksize)
# - and the so-called Harris detector-free parameter (k)
corners = cv2.cornerHarris( img_gray, 2, 5, 0.04 )

plt.clf()
plt.imshow( corners, cmap='gray' )
FILESAVE = 'TEST_IMG_3.pdf'
plt.savefig(FILESAVE)
os.system('pdfcrop ' + FILESAVE + ' ' + FILESAVE)

