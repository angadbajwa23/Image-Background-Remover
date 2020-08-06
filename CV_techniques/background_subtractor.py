import cv2
import numpy

cap=cv2.VideoCapture(0)
if cap.isOpened():
    ret,frame=cap.read()
else :
    ret=False
fgbg=cv2.createBackgroundSubtractorMOG2()
knn=cv2.createBackgroundSubtractorKNN()
while ret:
    ret,frame=cap.read()
    fgmask=fgbg.apply(frame)
    knnmask=knn.apply(frame)
    cv2.imshow('original',frame)
    cv2.imshow('-background_MOG',fgmask)
    cv2.imshow('-background_knn', knnmask)

    if(cv2.waitKey(27))==1:
        break

cv2.waitKey(0)
cv2.destroyAllWindows()
cap.release()
