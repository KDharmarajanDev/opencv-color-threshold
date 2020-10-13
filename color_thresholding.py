import numpy as np
import cv2 as cv

cap = cv.VideoCapture(0)

while(True):
    ret, frame = cap.read()
    original = frame
    # Color Thresholding
    lower_bound = (38,120,120)
    upper_bound = (99,191,185)
    mask = cv.inRange(frame,lower_bound,upper_bound)

    #Eroding
    mask = cv.morphologyEx(mask,cv.MORPH_OPEN,np.ones((10,10),np.uint8))

    mask_bgr = cv.cvtColor(mask, cv.COLOR_GRAY2BGR)
    frame = cv.bitwise_and(frame, mask_bgr)

    # Getting Contours
    _, contours, _ = cv.findContours(mask,cv.RETR_TREE,cv.CHAIN_APPROX_SIMPLE)
    cv.drawContours(frame,contours,-1,(100,0,225),3)
    if len(contours) > 0:
        largest_countour = max(contours,key=cv.contourArea)

    # Getting Bounding Box
    if len(contours) > 0:
        rect = cv.minAreaRect(largest_countour)
        box = cv.boxPoints(rect)
        box = box.astype(np.int32)
        cv.drawContours(frame,[box],0,(255,0,0),10)

    cv.imshow('frame',np.hstack((original,frame)))
    if cv.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv.destroyAllWindows()