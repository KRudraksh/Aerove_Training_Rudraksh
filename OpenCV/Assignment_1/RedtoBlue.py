import cv2
import numpy as np

path=r'/home/rudy-001/git_workspace/Aerove_Training_Rudraksh/OpenCV/Assignment_1/Original.jpeg'
frame=cv2.imread(path)

cv2.imshow('Original',frame)
hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
lower_red = np.array([30,150,50])
upper_red = np.array([255,255,180])

mask = cv2.inRange(hsv, lower_red, upper_red)
frame[mask>0]=(255,0,0)
cv2.imshow('Converted',frame)
cv2.waitKey(0)
