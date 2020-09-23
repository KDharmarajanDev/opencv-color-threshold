import numpy as np
import cv2 as cv

cap = cv.VideoCapture(0)

while(True):
    ret, frame = cap.read()
    frame = cv.cvtColor(frame, cv.COLOR_BGR2RGB)
    mask = cv.inRange(frame,(120,120,30),(200,200,100))
    mask_rgb = cv.cvtColor(mask, cv.COLOR_GRAY2RGB)
    frame = cv.bitwise_and(frame, mask_rgb)
    cv.imshow('frame',frame)
    if cv.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv.destroyAllWindows()