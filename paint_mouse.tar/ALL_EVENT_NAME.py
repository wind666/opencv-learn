# -*- coding: utf-8 -*-
"""
Created on Sun Jan 5 11:29:15 2014
@author: duan
"""
import cv2
events=[i for i in dir(cv2) if 'EVENT'in i]
print (events)
