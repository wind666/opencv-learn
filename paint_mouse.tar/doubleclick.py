# -*- coding: utf-8 -*-
"""
Created on Sun Jan 5 11:31:53 2014
@author: duan
"""
import cv2
import numpy as np
#mouse callback function
def draw_circle(event,x,y,flags,param):
    if event==cv2.EVENT_LBUTTONDBLCLK:
        #10 is the length of the circle
        cv2.circle(img,(x,y),10,(255,0,0),-1)
# 创建图像与窗口并将窗口与回调函数绑定
img=np.zeros((512,512,3),np.uint8)
cv2.namedWindow('image')
cv2.setMouseCallback('image',draw_circle)
while True:
    cv2.imshow('image',img)
    if cv2.waitKey(20)&0xFF==27:#press "ESC"button to quit
        break
cv2.destroyAllWindows()
