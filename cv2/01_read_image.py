import cv2
import matplotlib.pyplot as plt
import sys
import os

img_bgr = cv2.imread( sys.argv[1] )
img_rgb = cv2.cvtColor( img_bgr, cv2.COLOR_BGR2RGB )

plt.figure(figsize=(12,6))
plt.subplot(121)
plt.imshow(img_bgr)
plt.subplot(122)
plt.imshow(img_rgb)

FILESAVE = 'TEST_IMG_1.pdf'
plt.savefig(FILESAVE)
os.system('pdfcrop ' + FILESAVE + ' ' + FILESAVE)


