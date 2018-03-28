import numpy as np
import cv2
import matplotlib.pyplot as plt

# create a black image
img_bgr = np.zeros( (512,512,3), np.uint8 )

# diagonal blue line with thickness 5px
img_bgr = cv2.line( img_bgr, (0,0), (511,511), (255,0,0), 5 )

# rectangle
img_bgr = cv2.rectangle( img_bgr, (384,0), (510,128), (0,255,0), 3 )

# circle
img_bgr = cv2.circle( img_bgr, (447,63), 63, (0,128,128), -1 )

# ellipse
img_bgr = cv2.ellipse( img_bgr, (256,256), (100,50), 0, 0, 180, 255, -1 )

img_rgb = cv2.cvtColor( img_bgr, cv2.COLOR_BGR2RGB )

FILESAVE = 'TEST_IMG_06_drawing.jpg'

plt.clf()
plt.imshow(img_rgb)
plt.xticks([])
plt.yticks([])
plt.savefig(FILESAVE)