import cv2

cap = cv2.VideoCapture(0)

if cap.isOpened():
    ret, frame = cap.read()
else:
    ret = False

while ret:
    ret, frame = cap.read()
    output = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    edges=cv2.Canny(output,50,300)
    cv2.imshow("Live Feed", frame)
    #cv2.imshow("Gray", output)

    cv2.imshow("Edges", edges)
    ret, thres2 = cv2.threshold(edges, 200, 255, cv2.THRESH_BINARY)

    res = cv2.bitwise_and(frame, frame, mask=edges)


    cv2.imshow('output', res)

    if (cv2.waitKey(1)) == 27:
        break
cv2.destroyAllWindows()
cap.release()

