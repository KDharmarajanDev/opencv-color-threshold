import numpy as np
import cv2 as cv


def rescale_frame(frame, percent=75):
    width = int(frame.shape[1] * percent/ 100)
    height = int(frame.shape[0] * percent/ 100)
    dim = (width, height)
    return cv.resize(frame, dim, interpolation =cv.INTER_AREA)

cap = cv.VideoCapture('/Users/karthikdharmarajan/Documents/URobotics/Course Footage/GOPR1146.MP4')

while(cap.isOpened()):
    ret, img_in = cap.read()
    
    if ret:
        img_in = rescale_frame(img_in,30)
        blue, green, red = cv.split(img_in)

        blue_hist = cv.equalizeHist(blue)
        green_hist = cv.equalizeHist(green)
        red_hist = cv.equalizeHist(red)

        cv.imshow('img_in',img_in)
        cv.imshow('blue_hist',blue_hist)
        cv.imshow('green_hist',green_hist)
        cv.imshow('red_hist', red_hist)
    if cv.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv.destroyAllWindows()