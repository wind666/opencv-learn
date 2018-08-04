import numpy as np
import cv2

cap = cv2.VideoCapture(0)
#set the size of the window
cap.set(3,620)
cap.set(4,480)
#write the video as the name:output.avi---based on python352
fourcc = cv2.VideoWriter_fourcc(*'XVID')
#in python2,    fourcc = cv2.cv.FOURCC(*'XVID')   can be useful
out = cv2.VideoWriter('output.avi',fourcc,20.0,(640,480))

while(True):
# Capture frame-by-frame
    ret, frame = cap.read()
    #wrie video
    #rotate 180--0,no rotate--other integer
    frame=cv2.flip(frame,2)
    out.write(frame)

    # Our operations on the frame come here
    #gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Display the resulting frame
    cv2.imshow('frame',gray)
    if cv2.waitKey(25) & 0xFF == ord('q'):
        break

    # When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
