import cv2
import numpy as np

cap=cv2.VideoCapture(0)
if cap.isOpened():
    ret,frame=cap.read()
else :
    ret=False
fgbg=cv2.createBackgroundSubtractorMOG2()

while ret:
    ret,frame=cap.read()
    fgmask=fgbg.apply(frame)
    cv2.imshow('original', frame)
    cv2.imshow('-background_MOG', fgmask)



    ret,thres2=cv2.threshold(fgmask,127,255,cv2.THRESH_BINARY)
    res = cv2.bitwise_and(frame, frame, mask=thres2)


    cv2.imshow('output',res)


    if(cv2.waitKey(27))==1:
        break

cv2.waitKey(0)
cv2.destroyAllWindows()
cap.release()