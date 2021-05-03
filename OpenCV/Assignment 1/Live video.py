import cv2
import numpy as np


cap = cv2.VideoCapture(0)

currentFrame = 0
while(True):
    ret, frame = cap.read()
    frame = cv2.flip(frame,1)

    cv2.imshow("Live",frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


    currentFrame += 1

cap.release()
cv2.destroyAllWindows()
