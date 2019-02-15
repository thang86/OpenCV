import cv2
import  numpy as np

canvas = np.zeros((300,300,3),dtype='uint8')
green = (0,255,0)
cv2.line(canvas,(0,0),(300,300),green)


red = (0,0,255)
cv2.line(canvas,(0,300),(300,0),red,3)
cv2.imshow('Canvas2',canvas)

cv2.rectangle(canvas,(10,10),(60,60),green)
cv2.imshow('Canvas2',canvas)

blue = (255,0,0)
cv2.rectangle(canvas,(200,50),(225,120),blue,-1)
cv2.imshow('Canvas2',canvas)
cv2.waitKey(0)