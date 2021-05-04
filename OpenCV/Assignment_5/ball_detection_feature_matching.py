import numpy as np
import cv2

pathv=r'/home/rudy-001/git_workspace/Aerove_Training_Rudraksh/OpenCV/Assignment_5/messi.mp4'
pathb=r'/home/rudy-001/git_workspace/Aerove_Training_Rudraksh/OpenCV/Assignment_5/ball.jpg'
path_xml=r'/home/rudy-001/git_workspace/Aerove_Training_Rudraksh/OpenCV/Assignment_5/'
ball_cascade  = cv2.CascadeClassifier(path_xml + 'ball.xml')
img = cv2.imread(pathb)
cap = cv2.VideoCapture(pathv)

while True:
	ret,img = cap.read()
	gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

	balls = ball_cascade.detectMultiScale(gray,1.1, 5, 8, (16, 16))
	for ball in balls:
		x = ball[0] + int(ball[2]*0.5)
		y = ball[1] + int(ball[3]*0.5)
		cv2.circle(img,(x,y),int(ball[2]*0.5),(0,255,0),5)
	
	if cv2.waitKey(20) & 0xFF == ord('q'):
		break
	cv2.imshow("football",img)


cv2.destroyAllWindows()