import numpy as np
import cv2

img = np.zeros((512,512,3))

img = cv2.line(img, (0,0), (511,511), (255,255,0), 5)

cv2.imwrite("TEMP_16_draw_line.jpg", img)