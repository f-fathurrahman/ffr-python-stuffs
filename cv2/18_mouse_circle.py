import numpy as np
import cv2

def print_all_cv2_events():
    events = [i for i in dir(cv2) if "EVENT" in i]
    for e in events:
        print(e)

def draw_circle(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDBLCLK:
        cv2.circle(img, (x,y), 100, (255,0,0), -1)

print_all_cv2_events()

img = np.zeros((512,512,3), np.uint8)
cv2.namedWindow("Test image")
cv2.setMouseCallback("Test image", draw_circle)

while(True):
    cv2.imshow("Test image", img)
    if cv2.waitKey(20) & 0xFF == 27:  # ESC key
        break
cv2.destroyAllWindows()



