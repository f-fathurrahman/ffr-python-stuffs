import numpy as np
import cv2
import sys

cap = cv2.VideoCapture(sys.argv[1])

while( cap.isOpened() ):

    ret, frame = cap.read()

    rgb = cv2.cvtColor( frame, cv2.COLOR_BGR2RGB )
    
    cv2.imshow('frame', rgb)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

