import cv2
import numpy as np

cap = cv2.VideoCapture("/home/qt/Vision/output.avi")
while True:
    # get a frame
    ret, frame = cap.read()
    # show a frame
    cv2.imshow("capture", frame)
    if cv2.waitKey(100) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows() 
