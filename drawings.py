import cv2
import  numpy as np

canvas = np.zeros((300,300,3),dtype='uint8')
green = (0,255,0)
cv2.line(canvas,(0,0),(150,150),green)

cv2.imshow('Cannn',canvas)
cv2.waitKey(0)

