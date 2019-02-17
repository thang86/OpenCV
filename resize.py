import cv2
import argparse
import imutils
import numpy as np

ap = argparse.ArgumentParser()
ap.add_argument('-i','--image',required=True,help='Duong dan hinh anh')
args = vars(ap.parse_args())
image = cv2.imread(args['image'])
print(image.shape[1])
r = 60 / image.shape[1]
dim = (150,int(image.shape[0]*0.5))
resized = cv2.resize(image,dim,interpolation=cv2.INTER_AREA)
cv2.imshow('Anh goc',image)
cv2.imshow('Resizzwe',resized)
cv2.waitKey(0)