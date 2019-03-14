import numpy as np
import cv2

img = np.zeros((512,512,3))

# need top-left corner and bottom-right corner of rectangle
img = cv2.rectangle(img, (200,0), (510,128), (50,255,10), 3)

cv2.imwrite("TEMP_17_draw_rectangle.jpg", img)