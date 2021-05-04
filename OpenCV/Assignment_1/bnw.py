import cv2
path=r'/home/rudy-001/git_workspace/Aerove_Training_Rudraksh/OpenCV/Assignment_1/Original.jpeg'
img=cv2.imread(path)
grayimg=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY) 
(thresh,bnw)=cv2.threshold(grayimg,127,255,cv2.THRESH_BINARY) 
cv2.imshow('black and white image',bnw)
cv2.imshow('grayscale image',grayimg)
cv2.imshow('original image',img)
cv2.waitKey(0)