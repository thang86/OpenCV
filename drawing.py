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

# ve hinh tron

canvas = np.zeros((300,300,3),dtype='uint8')
(dx,dy) = (canvas.shape[1]//2,canvas.shape[0]//2)
white =(255,255,255)

for r in range(0,175,25):
    cv2.circle(canvas,(dx,dy),r,white)

cv2.imshow('Canvas3',canvas)
cv2.waitKey(0)

for i in range(0,25):
    radius = np.random.randint(5,high=200)
    color = np.random.randint(0,high=256,size=(3,)).tolist()
    pt = np.random.randint(0,high=300,size=(2,))
    cv2.circle(canvas,tuple(pt),radius,color,-1)
cv2.imshow('Canvas3',canvas)
cv2.waitKey(0)

