import numpy as np
import cv2

# Create a black image
img=np.zeros((512,512,3), np.uint8)

# Draw a diagonal blue line with thickness of 5 px

cv2.line(img,(0,0),(511,511),(255,0,0),5)

cv2.rectangle(img,(384,0),(510,128),(0,255,0),3)

cv2.circle(img,(447,63), 63, (0,0,255), -1)
#changed circle,looks like an egg
cv2.ellipse(img,(256,256),(100,50),0,0,180,255,-1)

#add text on the picture
font=cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img,'OpenCV',(10,500), font, 4,(255,255,255),2)

#connects everything above
#Why they warned no winname and no imshow when I run the two line below on the  terminal??
winname = 'example'
cv2.namedWindow(winname)
cv2.imshow(winname, img)
cv2.waitKey(0)#press any key to close the picture
cv2.destroyWindow(winname)
