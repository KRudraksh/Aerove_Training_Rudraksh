import imutils
import cv2
path=r'/home/rudy-001/git_workspace/Aerove_Training_Rudraksh/OpenCV/Assignment_4/original.jpeg'

class Shape_parameters:
	def __init__(self):
		pass
	def detect(self, c):
		shape = "unidentified"
		peri = cv2.arcLength(c, True)
		approx = cv2.approxPolyDP(c, 0.04 * peri, True)

		if len(approx) == 3:
			shape = "triangle"
		
		elif len(approx) == 4:
			(x, y, w, h) = cv2.boundingRect(approx)
			asp_rat = w / float(h)
			if asp_rat > 0.95 and asp_rat < 1.05:    #this is because approxPolyDP has a variance of 5%
				shape = "square"
			elif asp_rat > 0.712 and asp_rat < 0.814:
				shape = "rhombus"
			else:
				shape = "rectangle"  
		
		else:
			(x,y),radius = cv2.minEnclosingCircle(approx)
			center = (int(x),int(y))
			radius = int(radius)
			if len(approx) == 8:
				shape = "circle"
			else:
				shape = "oval"
		
		return shape

image = cv2.imread(path)
assert not isinstance(image,type(None)), 'image not found'
resize = imutils.resize(image, width=300)
ratio = image.shape[0] / float(resize.shape[0])

gray = cv2.cvtColor(resize, cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(gray, (5, 5), 0)
thresh = cv2.threshold(blurred, 150, 255, cv2.THRESH_BINARY)[1]

contours = cv2.findContours(thresh.copy(), cv2.RETR_LIST , cv2.CHAIN_APPROX_SIMPLE)
contours = imutils.grab_contours(contours)
detecte_shape = Shape_parameters()

for c in contours:
	M = cv2.moments(c)
	
	cX = int((M["m10"] / M["m00"]) * ratio)
	cY = int((M["m01"] / M["m00"]) * ratio)
	
	shape = detecte_shape.detect(c)
 	
	c = c.astype("float")
	c *= ratio
	c = c.astype("int")
	cv2.drawContours(image, [c], -1, (0, 255, 0), 2)
	cv2.putText(image, shape, (cX, cY), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 2)


cv2.imshow("Image", image)
cv2.waitKey(0)
cv2.destroyAllWindows()